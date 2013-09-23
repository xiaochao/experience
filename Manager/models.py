from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=60)
