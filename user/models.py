from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    cpf = models.CharField(unique=True, max_length=14)
    cargo = models.CharField(max_length=40)
    email = models.EmailField(max_length=100, unique=True)

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['email', 'cargo']

    def __str__(self):
        return f'{self.username} - {self.cpf}'
