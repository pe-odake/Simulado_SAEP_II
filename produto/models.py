from django.db import models
from user.models import User

class Produto(models.Model):
    codigo = models.IntegerField(primary_key=True, unique=True)
    nome = models.CharField(max_length=80)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    fabricante = models.CharField(max_length=80)
    categoria = models.CharField(max_length=50)
    estoque_limite = models.IntegerField()
    altura = models.FloatField()
    comprimento = models.FloatField()
    largura = models.FloatField()
    peso = models.FloatField()
    imagem = models.ImageField(upload_to="produto/", null=True, blank=True)

    def __str__(self):
        return f'{self.codigo} - {self.nome}'
    
class Entrada(models.Model):
    codigo = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="produto_entrando")
    data = models.DateField()
    quantidade = models.IntegerField()
    fornecedor = models.CharField(max_length=80)
    lote = models.CharField(max_length=80)
    
    def __str__(self):
        return f'{self.pk} - entrada de {self.codigo}'
    
class Saida(models.Model):
    codigo = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="produto_saindo")
    data = models.DateField()
    quantidade = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario")
    lote = models.CharField(max_length=80)
    
    def __str__(self):
        return f'{self.pk} - saida de {self.codigo}'