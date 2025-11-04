from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class User(AbstractUser):
    cpf = models.CharField(unique=True, max_length=14)
    cargo = models.CharField(max_length=40)
    email = models.EmailField(max_length=100, unique=True)

    REQUIRED_FIELDS = ['cpf', 'email', 'cargo']