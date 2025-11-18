from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.views.generic import CreateView, TemplateView
from .models import User
from .forms import LoginForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from produto.models import Produto, Entrada, Saida
from django.db.models import Sum

class LoginView(LoginView): 
    template_name = "user/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy("home")

class LogoutView(LogoutView):
    next_page = "login"


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'user/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_produtos'] = Produto.objects.count()
        context['total_entradas'] = Entrada.objects.count()
        context['total_saidas'] = Saida.objects.count()
        
        context['ultimas_entradas'] = Entrada.objects.order_by('-id')[:5]
        context['ultimas_saidas'] = Saida.objects.order_by('-id')[:5]

        produtos_criticos = []

        for produto in Produto.objects.all():
            entradas = Entrada.objects.filter(codigo=produto).aggregate(
                total=Sum('quantidade')
            )['total'] or 0

            saídas = Saida.objects.filter(codigo=produto).aggregate(
                total=Sum('quantidade')
            )['total'] or 0

            estoque_atual = entradas - saídas

            if estoque_atual < produto.estoque_limite:
                produtos_criticos.append({
                    "produto": produto,
                    "estoque_atual": estoque_atual,
                    "limite": produto.estoque_limite,
                })

        context["produtos_criticos"] = produtos_criticos
        context["qtd_produtos_criticos"] = len(produtos_criticos)

        return context