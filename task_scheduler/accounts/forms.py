from django import forms
from django.contrib.auth.models import User
from accounts.models import UserInfo
from django.core.exceptions import ValidationError


class UserInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirmation = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        password_confirmation = cleaned_data['password_confirmation']
        print(cleaned_data)
        if password != password_confirmation:
            raise ValidationError('MAKE SURE PASSWORD ARE THE SAME')


class UserAdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('avatar_img', 'department', 'grade')

