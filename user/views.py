# views.py
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CPFAuthenticationForm

class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    authentication_form = CPFAuthenticationForm
    
    def form_valid(self, form):
        # Aqui o CPF já foi limpo pelo form.clean_username()
        cpf = form.cleaned_data['username']
        password = form.cleaned_data['password']
        
        # O Django vai automaticamente buscar pelo username (que é o CPF)
        user = authenticate(self.request, username=cpf, password=password)
        
        if user is not None:
            login(self.request, user)
            messages.success(self.request, f'Bem-vindo, {user.first_name or user.username}!')
            return redirect('home')
        else:
            messages.error(self.request, 'CPF ou senha inválidos.')
            return self.form_invalid(form)

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'user/home.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso.')
    return redirect('login')