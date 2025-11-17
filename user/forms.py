from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"autofocus": True})
    )

    error_messages = {
        'invalid_login': (
            "E-mail ou senha incorretos. Verifique suas credenciais e tente novamente."
        ),
        'inactive': ("Esta conta está inativa."),
    }