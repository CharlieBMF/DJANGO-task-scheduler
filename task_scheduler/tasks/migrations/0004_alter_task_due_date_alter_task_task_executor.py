# Generated by Django 4.0.5 on 2022-07-10 21:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0003_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_executor',
            field=models.ManyToManyField(blank=True, related_name='task_executor', to=settings.AUTH_USER_MODEL),
        ),
    ]
