from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Produto, Entrada
from .forms import ProdutoForm, EntradaForm
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