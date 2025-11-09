from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Produto, Entrada, Saida
from .forms import ProdutoForm, EntradaForm, SaidaForm
from django.urls import reverse_lazy

# PRODUTOS

class ListProdutosView(ListView):
    model = Produto
    template_name = 'produto/estoque.html'
    context_object_name = 'produtos'
    
class CreateProdutosView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/form.html'
    success_url = reverse_lazy('list_produtos')
    
class EditProdutosView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/form.html'
    success_url = reverse_lazy('list_produtos')

class DeleteProdutoView(DeleteView):
    model = Produto
    success_url = reverse_lazy('list_produtos')

# -------------------------------------------------

# ENTRADAS

class ListEntradasView(ListView):
    model = Entrada
    template_name = 'produto/entrada.html'
    context_object_name = 'entradas'
    
class CreateEntradasView(CreateView):
    model = Entrada
    form_class = EntradaForm
    template_name = 'produto/form.html'
    success_url = reverse_lazy('list_entradas')

class EditEntradasView(UpdateView):
    model = Entrada
    form_class = EntradaForm
    template_name = 'produto/form.html'
    success_url = reverse_lazy('list_entradas')

class DeleteEntradasView(DeleteView):
    model = Produto
    success_url = reverse_lazy('list_entradas')

# -------------------------------------------------

# SAIDAS

class ListSaidasView(ListView):
    model = Saida
    template_name = 'produto/saidas.html'
    context_object_name = 'saidas'
    
class CreateSaidasView(CreateView):
    model = Saida
    form_class = SaidaForm
    template_name = 'produto/form.html'
    success_url = reverse_lazy('list_entradas')

class EditSaidasView(UpdateView):
    model = Saida
    form_class = SaidaForm
    template_name = 'produto/form.html'
    success_url = reverse_lazy('list_entradas')

class DeleteSaidasView(DeleteView):
    model = Saida
    success_url = reverse_lazy('list_entradas')