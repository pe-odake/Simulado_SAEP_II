from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView as AuthLoginView
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
class LoginView(AuthLoginView):
    template_name = 'user/login.html'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return self.form_invalid(form)
        
class HomeView(View):
    def get(self, request):
        return render(request, 'user/home.html')