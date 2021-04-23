from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=64)
    email = models.EmailField()


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=64)
    email = models.EmailField()