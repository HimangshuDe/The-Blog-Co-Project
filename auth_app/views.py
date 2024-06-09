from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.contrib.auth import logout
from django.urls import reverse

# Create your views here.

def user_login(request):
    return HttpResponse('Login Page')

def user_register(request):
    # return HttpResponse('Register Page')
    return render(request, 'auth_app/register.html')

def user_logout(request):
    logout(request)
    return HttpResponsePermanentRedirect(reverse('index'))