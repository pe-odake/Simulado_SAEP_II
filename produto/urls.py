from django.urls import path
from .views import ListProdutosView, CreateProdutosView, EditProdutosView, DeleteProdutoView
from .views import ListEntradasView, CreateEntradasView, EditEntradasView, DeleteEntradasView
from .views import ListSaidasView, CreateSaidasView, EditSaidasView, DeleteSaidasView

urlpatterns = [
    path('', ListProdutosView.as_view(), name='list_produtos'),
    path('add/', CreateProdutosView.as_view(), name='create_produtos'),
    path('edit/<int:pk>/', EditProdutosView.as_view(), name='edit_produto'),
    path('delete/<int:pk>/', DeleteProdutoView.as_view(), name='delete_produto'),

    path('entradas/', ListEntradasView.as_view(), name='list_entradas'),
    path('entradas/add', CreateEntradasView.as_view(), name='create_entradas'),
    path('entradas/edit/<int:pk>/', EditEntradasView.as_view(), name='edit_entradas'),
    path('entradas/delete/<int:pk>/', DeleteEntradasView.as_view(), name='delete_entradas'),

    path('saidas/', ListSaidasView.as_view(), name='list_saidas'),
    path('saidas/add', CreateSaidasView.as_view(), name='create_saidas'),
    path('saidas/edit/<int:pk>/', EditSaidasView.as_view(), name='edit_saidas'),
    path('saidas/delete/<int:pk>/', DeleteSaidasView.as_view(), name='delete_saidas'),
]
