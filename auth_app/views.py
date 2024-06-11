from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse

from auth_app.forms import LoginForm, CustomUserCreationForm

# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        return HttpResponsePermanentRedirect(reverse('index'))
    form = LoginForm()  
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user_email = form.cleaned_data['email']
            user_password = form.cleaned_data['password']
            user = authenticate(email=user_email, password = user_password)

            if user is not None:
                login(request, user)

                if request.GET.get('next'):
                    return HttpResponsePermanentRedirect(request.GET.get('next'))

                return HttpResponsePermanentRedirect(reverse('index'))

    return render(request, 'auth_app/login.html', {'form':form})

def user_register(request):
    # return HttpResponse('Register Page')
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print('validated')
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'auth_app/register.html', {'form':form})

def user_logout(request):
    logout(request)
    return HttpResponsePermanentRedirect(reverse('index'))