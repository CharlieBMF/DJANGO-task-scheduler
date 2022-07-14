from django import forms
from tasks.models import Task
from django.core.exceptions import ValidationError


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'responsible_department', 'description', 'importance']
