from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    cargo = models.CharField(max_length=40)
    cpf = models.CharField(max_length=11, unique=True)

    REQUIRED_FIELDS = ["email", "cpf"]

    def __str__(self):
        return self.email