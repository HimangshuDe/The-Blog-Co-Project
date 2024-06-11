from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse

from auth_app.forms import LoginForm, CustomUserCreationForm

# Create your views here.

def user_login(request):
    return HttpResponse('Login Page')

def user_register(request):
    # return HttpResponse('Register Page')
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print('validated')
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'auth_app/register.html', {'forms':form})

def user_logout(request):
    logout(request)
    return HttpResponsePermanentRedirect(reverse('index'))