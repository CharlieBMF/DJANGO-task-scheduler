from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from tasks.models import Task
from tasks.forms import TaskForm
from accounts.models import UserInfo
from django.urls import reverse
from django.core.exceptions import ValidationError

# Create your views here.
class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks_list'


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task_details'


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


def task_get(request, pk):
    task = Task.objects.get(id=pk)
    task.task_executor = UserInfo.objects.filter(user=request.user.id)[0]
    task.due_date = request.POST.get('due_date')
    task.status = 'INP'
    task.save()
    return redirect('tasks:task_detail', pk=pk)


def task_finish(request, pk):
    task = Task.objects.get(id=pk)
    task.status = 'DONE'
    task.save()
    return redirect('tasks:task_detail', pk=pk)