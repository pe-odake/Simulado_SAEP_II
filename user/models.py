from django.db import models
from django.contrib.auth.models import AbstractUser,    UserManager

class User(AbstractUser):
    cpf = models.FloatField(primary_key=True, unique=True, max_length=14)
    cargo = models.CharField(max_length=40)
    email = models.CharField(max_length=100)

    objects = UserManager() 

    REQUIRED_FIELDS = ['cpf', 'username', 'email', 'password', 'cargo']