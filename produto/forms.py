from django import forms
from .models import Produto, Entrada

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['codigo', 'nome', 'preco', 'fabricante', 'categoria', 'estoque_limite', 'altura', 'comprimento', 'largura', 'peso', 'imagem']
        
class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['codigo', 'realizado_por', 'data', 'quantidade', 'fornecedor', 'lote']