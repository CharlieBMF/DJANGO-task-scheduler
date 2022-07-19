from django import forms
from tasks.models import Task
from accounts.models import UserInfo


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'responsible_department', 'description', 'importance']


DEPARTMENT_USERS = [(y.user, y.user) for y in UserInfo.objects.all()]


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskAsignementForm(forms.Form):
    user_to_asign = forms.ChoiceField(choices=DEPARTMENT_USERS)
    due_date = forms.DateField(widget=DateInput)
