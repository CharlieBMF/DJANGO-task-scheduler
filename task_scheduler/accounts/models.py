from django.db import models
from django.contrib.auth.models import User

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
GRADES = [
    ('OP', 'OPERATIONAL'),
    ('SP', 'SPECIALIST'),
    ('TL', 'TEAM LEADER'),
    ('SU', 'SUPERVISOR'),
    ('MN', 'MANAGER'),
]


class UserInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Special attributes
    avatar_img = models.ImageField(upload_to='profile_avatar', blank=True)
    department = models.CharField(max_length=2, choices=DEPARTMENTS, default='NA')
    grade = models.CharField(max_length=2, choices=GRADES, default='OP')

    def __str__(self):
        return self.user.username
