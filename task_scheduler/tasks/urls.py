from django.urls import path
from tasks.views import TaskListView, TaskDetailView, task_create, \
                        task_get, task_finish


app_name = 'tasks'

urlpatterns = [
    path('list', TaskListView.as_view(), name='task_list'),
    path('task_detail/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('task_creation', task_create, name='task_creation'),
    path('task_get/<int:pk>', task_get, name='task_get'),
    path('task_finish/<int:pk>', task_finish, name='task_finish')

]