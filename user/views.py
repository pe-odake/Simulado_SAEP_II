from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.views.generic import CreateView
from .models import User
from .forms import LoginForm
from django.urls import reverse_lazy
from django.shortcuts import render
    
class LoginView(LoginView):
    template_name = "user/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy("home")

class LogoutView(LogoutView):
    next_page = "login"

class HomeView(View):
    def get(self, request):
        return render(request, 'user/home.html')