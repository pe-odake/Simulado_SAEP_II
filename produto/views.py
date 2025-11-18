from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Produto, Entrada, Saida
from .forms import ProdutoForm, EntradaForm, SaidaForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# PRODUTOS

class ListProdutosView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'produto/estoque.html'
    context_object_name = 'produtos'
    
class CreateProdutosView(LoginRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/form.html'
    success_url = reverse_lazy('list_produtos')
    
class EditProdutosView(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/form.html'
    success_url = reverse_lazy('list_produtos')

class DeleteProdutoView(LoginRequiredMixin, DeleteView):
    model = Produto
    success_url = reverse_lazy('list_produtos')

# -------------------------------------------------

# ENTRADAS

class ListEntradasView(LoginRequiredMixin, ListView):
    model = Entrada
    template_name = 'produto/entrada.html'
    context_object_name = 'entradas'
    
class CreateEntradasView(LoginRequiredMixin, CreateView):
    model = Entrada
    form_class = EntradaForm
    template_name = 'produto/form.html'
    success_url = reverse_lazy('list_entradas')

class EditEntradasView(LoginRequiredMixin, UpdateView):
    model = Entrada
    form_class = EntradaForm
    template_name = 'produto/form.html'
    success_url = reverse_lazy('list_entradas')

class DeleteEntradasView(LoginRequiredMixin, DeleteView):
    model = Produto
    success_url = reverse_lazy('list_entradas')

# -------------------------------------------------

# SAIDAS

class ListSaidasView(LoginRequiredMixin, ListView):
    model = Saida
    template_name = 'produto/saidas.html'
    context_object_name = 'saidas'
    
class CreateSaidasView(LoginRequiredMixin, CreateView):
    model = Saida
    form_class = SaidaForm
    template_name = 'produto/form.html'
    success_url = reverse_lazy('list_saidas')

class EditSaidasView(LoginRequiredMixin, UpdateView):
    model = Saida
    form_class = SaidaForm
    template_name = 'produto/form.html'
    success_url = reverse_lazy('list_saidas')

class DeleteSaidasView(LoginRequiredMixin, DeleteView):
    model = Saida
    success_url = reverse_lazy('list_saidas')