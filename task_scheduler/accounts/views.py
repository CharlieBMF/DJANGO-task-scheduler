from django.shortcuts import render
from accounts.forms import UserInfoForm, UserAdditionalInfoForm
from accounts.models import UserInfo
from django.views.generic import ListView, DetailView


def register(request):

    registered = False

    if request.method == 'POST':
        user_info_form = UserInfoForm(data=request.POST)
        user_additional_info_form = UserAdditionalInfoForm(data=request.POST)

        if user_info_form.is_valid() and user_additional_info_form.is_valid():
            user = user_info_form.save()
            user.set_password(user.password)
            user.save()

            additional_info = user_additional_info_form.save(commit=False)
            additional_info.user = user
            if 'avatar_img' in request.FILES:
                additional_info.avatar_img = request.FILES['avatar_img']

            additional_info.save()
            registered = True
    else:
        user_info_form = UserInfoForm()
        user_additional_info_form = UserAdditionalInfoForm()

    return render(request, 'registration.html', {'user_form': user_info_form,
                                                 'additional_user_form': user_additional_info_form,
                                                 'registered': registered})


class UserListView(ListView):
    model = UserInfo
    context_object_name = 'users_list'


class UserDetailView(DetailView):
    model = UserInfo
    context_object_name = 'userinfo_details'
