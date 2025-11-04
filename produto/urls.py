from django.urls import path
from .views import ListProdutosView, CreateProdutosView, EditProdutosView, DeleteProdutoView

urlpatterns = [
    path('', ListProdutosView.as_view(), name='list_produtos'),
    path('add/', CreateProdutosView.as_view(), name='create_produtos'),
    path('edit/<int:pk>/', EditProdutosView.as_view(), name='edit_produto'),
    path('delete/<int:pk>/', DeleteProdutoView.as_view(), name='delete_produto'),
]
