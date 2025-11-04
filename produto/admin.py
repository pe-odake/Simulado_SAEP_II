from django.contrib import admin
from .models import Produto, Entrada, Saida

admin.site.register(Produto)
admin.site.register(Entrada)
admin.site.register(Saida)