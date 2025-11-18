from django import forms
from .models import Produto, Entrada, Saida

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'fabricante', 'categoria', 'estoque_limite', 'altura', 'comprimento', 'largura', 'peso', 'imagem']
        
class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['realizado_por', 'data', 'quantidade', 'fornecedor', 'lote']

class SaidaForm(forms.ModelForm):
    class Meta:
        model = Saida
        fields = ['realizado_por', 'data', 'quantidade', 'user', 'lote']