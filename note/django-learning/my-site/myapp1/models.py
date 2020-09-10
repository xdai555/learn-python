from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class User(models.Model):
    # CharField类型不能为空,最少要指定一个长度
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
