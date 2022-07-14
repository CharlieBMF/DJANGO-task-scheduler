from django.urls import path
from accounts.views import register, UserListView, UserDetailView

app_name = 'accounts'

urlpatterns = [
    path('register', register, name='register'),
    path('users_list', UserListView.as_view(), name='userinfo_list'),
    path('user_detail/<int:pk>', UserDetailView.as_view(), name='userinfo_detail'),
]