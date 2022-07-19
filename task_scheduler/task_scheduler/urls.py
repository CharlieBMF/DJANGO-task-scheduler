from django.contrib import admin
from django.urls import path, include
from task_scheduler import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='homepage'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tasks/', include('tasks.urls', namespace='tasks')),
]
