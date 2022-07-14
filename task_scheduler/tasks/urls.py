from django.urls import path
from tasks.views import TaskListView, TaskDetailView, task_create


app_name = 'tasks'

urlpatterns = [
    path('list', TaskListView.as_view(), name='task_list'),
    path('task_detail/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('task_creation', task_create, name='task_creation'),

]