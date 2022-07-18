from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserInfo

# Create your models here.
DEPARTMENTS = [
    ('PR', 'PRODUCTION'),
    ('QA', 'QUALITY'),
    ('PE', 'PRODUCTION ENGINEERING'),
    ('SM', 'SALES MARKETING'),
    ('SE', 'SAFETY'),
    ('LP', 'LOGISTIC'),
    ('NA', 'UNDEFINED'),
]
TASK_IMPORTANCE = [
    ('HI', 'CRITICAL'),
    ('NO', 'NORMAL'),
    ('LO', 'LOW'),
]
STATUS = [
    ('NA', 'NOT ASSIGNED'),
    ('INP', 'IN PROGRESS'),
    ('DONE', 'DONE'),
]


class Task(models.Model):
    status = models.CharField(max_length=4, choices=STATUS, default='NA')
    task_creator = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, null=True, related_name='task_creator')
    task_executor = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, null=True, related_name='task_executor')
    responsible_department = models.CharField(max_length=2, choices=DEPARTMENTS, default='NA')
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_of_creation = models.DateField(auto_now=False, auto_now_add=True)
    due_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    finish_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    importance = models.CharField(max_length=2, choices=TASK_IMPORTANCE, default='LO')

    def __str__(self):
        return self.name

