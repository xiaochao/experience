from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=60)

class Bug(models.Model):
    title = models.CharField(max_length=200)
    explain = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=10)
    delete = models.BooleanField(default=False)
    kind = models.CharField(max_length=1000)