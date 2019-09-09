from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django import forms


class Employee(models.Model):
    user = models.OneToOneField(
        User, to_field='username', on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, primary_key=True)
    department = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=10)
    address = models.CharField(max_length=1000)
