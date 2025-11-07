# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('logout/', views.logout_view, name='logout'),
]