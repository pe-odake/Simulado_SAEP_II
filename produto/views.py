from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Produto
from .forms import ProdutoForm
from django.urls import reverse_lazy

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