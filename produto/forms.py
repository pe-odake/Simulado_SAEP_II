from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['codigo', 'nome', 'preco', 'fabricante', 'categoria', 'estoque_limite', 'altura', 'comprimento', 'largura', 'peso', 'imagem']