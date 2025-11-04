from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeView

urlpatterns = [
    path('', auth_views.LoginView.as_view(
        template_name='user/login.html'
    ), name='login'),
    path('home/', HomeView.as_view(), name='home'),
]