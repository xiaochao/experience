from django.db import models
from datetime import *


class User(models.Model):
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=60)

class Bug(models.Model):
    title = models.CharField(max_length=200)
    explain = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now=True, default=datetime.now())
    author = models.CharField(max_length=10)
    delete = models.BooleanField(default=False)
    kind = models.CharField(max_length=1000)

class CommentModel(models.Model):
    bug_id = models.CharField(max_length=20, default=1)
    comment = models.CharField(max_length=500)
    author = models.CharField(max_length=50, default='temp_user')
    delete = models.BooleanField(default=False)
    perfect = models.IntegerField(default=0)