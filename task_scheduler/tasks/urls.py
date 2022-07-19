from django.urls import path
from tasks.views import TaskListView, TaskDetailView, task_create, \
                        task_get, task_finish, TaskListViewByUser, \
                        TaskListViewByDepartment, task_asignement, \
                        statistics


app_name = 'tasks'

urlpatterns = [
    path('task_list', TaskListView.as_view(), name='task_list'),
    path('task_detail/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('task_creation', task_create, name='task_creation'),
    path('task_get/<int:pk>', task_get, name='task_get'),
    path('task_finish/<int:pk>', task_finish, name='task_finish'),
    path('task_list_user', TaskListViewByUser.as_view(), name='task_list_user'),
    path('task_list_department', TaskListViewByDepartment.as_view(), name='task_list_department'),
    path('task_asignement', task_asignement, name='task_asignement'),
    path('statistic', statistics, name='statistics'),
]
