from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from tasks.models import Task
from tasks.forms import TaskForm, TaskAsignementForm
from accounts.models import UserInfo, User
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from datetime import datetime


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks_list'


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task_details'


class TaskListViewByUser(ListView, LoginRequiredMixin):
    model = Task
    context_object_name = 'tasks_list'
    template_name = 'tasks/task_list_user.html'

    def get_queryset(self):
        return Task.objects.filter(task_executor=UserInfo.objects.filter(user=self.request.user.id)[0])


class TaskListViewByDepartment(ListView, LoginRequiredMixin):
    model = Task
    context_object_name = 'tasks_list'
    template_name = 'tasks/task_list_department.html'

    def get_queryset(self):
        return Task.objects.filter(
            responsible_department=UserInfo.objects.filter(user=self.request.user.id)[0].department
        )


@login_required
def task_create(request):
    if request.method == 'POST':
        task_form = TaskForm(data=request.POST)
        if task_form.is_valid():
            created_task = task_form.save(commit=False)
            created_task.task_creator = UserInfo.objects.filter(user=request.user.id)[0]
            created_task.save()
            return redirect('tasks:task_detail', pk=Task.objects.all()[len(Task.objects.all())-1].id)
    else:
        task_form = TaskForm()
    return render(request, 'tasks/task_form.html', {'task_form': task_form})


@login_required
def task_get(request, pk):
    task = Task.objects.get(id=pk)

    if task.responsible_department == UserInfo.objects.filter(user=request.user.id)[0].department or \
            task.responsible_department == 'NA':
        task.task_executor = UserInfo.objects.filter(user=request.user.id)[0]
        task.due_date = request.POST.get('due_date')
        task.status = 'INP'
        task.responsible_department = UserInfo.objects.filter(user=request.user.id)[0].department
        task.save()
    return redirect('tasks:task_detail', pk=pk)


@login_required
def task_finish(request, pk):
    task = Task.objects.get(id=pk)
    task.status = 'DONE'
    task.finish_date = datetime.today().strftime('%Y-%m-%d')
    task.save()
    return redirect('tasks:task_detail', pk=pk)


@login_required
def task_asignement(request):
    if request.method == 'POST':
        asignement_form = TaskAsignementForm(data=request.POST)
        if asignement_form.is_valid():
            asignemented_task = Task.objects.get(id=request.POST.get('custId'))
            asignemented_task.task_executor = UserInfo.objects.get(
                user=User.objects.get(username=asignement_form.cleaned_data['user_to_asign']))
            asignemented_task.due_date = asignement_form.cleaned_data['due_date']
            asignemented_task.status = 'INP'
            asignemented_task.responsible_department = UserInfo.objects.get(
                user=User.objects.get(username=asignement_form.cleaned_data['user_to_asign'])).department
            asignemented_task.save()
            return redirect('tasks:task_asignement')
    else:
        tasks_list = Task.objects.all()
        task_asignement_form = TaskAsignementForm()
        manager = False
        if len(UserInfo.objects.filter(user=request.user.id)) > 0 and \
                UserInfo.objects.filter(user=request.user.id)[0].grade == 'MN':
            manager = True
        return render(request, 'tasks/task_asignement.html', {'tasks_list': tasks_list,
                                                              'manager': manager,
                                                              'form': task_asignement_form,
                                                              })


def statistics(request):
    all_tasks_counter = Task.objects.count()
    not_asigned_task_counter = Task.objects.filter(status='NA').count()
    in_progress_task_counter = Task.objects.filter(status='INP').count()
    done_task_counter = Task.objects.filter(status='DONE').count()
    all_users_counter = UserInfo.objects.count()
    avg_tasks_per_user = round((in_progress_task_counter+done_task_counter)/all_users_counter, 2)

    amount_of_tasks = []
    result_of_groupby_task_executor = (Task.objects.values(
        'task_executor').annotate(dtask=Count('task_executor'))
              .order_by('-dtask'))
    if len(result_of_groupby_task_executor) > 5:
        sort_range = 5
    else:
        sort_range = len(result_of_groupby_task_executor)-1
    print(sort_range)
    for i in range(sort_range):
        dict = result_of_groupby_task_executor[i]
        dict['task_executor'] = str(UserInfo.objects.get(user=dict['task_executor']))
        amount_of_tasks.append(dict)
    amount_of_tasks_top5 = amount_of_tasks[0:5]
    amount_of_tasks_last5 = amount_of_tasks[:-6:-1]

    tasks_length = []
    tasks_total_length = 0
    for single_task in Task.objects.filter(status='DONE'):
        length = single_task.finish_date - single_task.date_of_creation
        dict = {single_task.name: int(str(length).split()[0])}
        tasks_length.append(dict)
        tasks_total_length += int(str(length).split()[0])
    if done_task_counter != 0:
        avg_tasks_length = f'{round(tasks_total_length / done_task_counter, 0)} days'
    else:
        avg_tasks_length = f'None of task is finished'
    return render(request, 'tasks/statistics.html', {'all_tasks_counter': all_tasks_counter,
                                                     'not_asigned_task_counter': not_asigned_task_counter,
                                                     'in_progress_task_counter': in_progress_task_counter,
                                                     'done_task_counter': done_task_counter,
                                                     'all_users_counter': all_users_counter,
                                                     'avg_tasks_per_user': avg_tasks_per_user,
                                                     'amount_of_tasks_top5': amount_of_tasks_top5,
                                                     'amount_of_tasks_last5': amount_of_tasks_last5,
                                                     'avg_tasks_length': avg_tasks_length
                                                     })




