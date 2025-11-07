# forms.py (crie este arquivo se não existir)
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User

class CPFAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='CPF', max_length=14)
    
    def clean_username(self):
        cpf = self.cleaned_data['username']
        # Remove caracteres não numéricos do CPF
        cpf = ''.join(filter(str.isdigit, cpf))
        return cpf