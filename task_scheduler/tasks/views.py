from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from tasks.models import Task
from tasks.forms import TaskForm
from accounts.models import UserInfo
from django.urls import reverse

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

