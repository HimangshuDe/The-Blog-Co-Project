from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from auth_app.forms import CustomUserChangeForm, LoginForm, CustomUserCreationForm
from auth_app.models import UserModel

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
            print(user_email, user_password)
            user = authenticate(email=user_email, password = user_password)
            print(user)

            if user is not None:
                login(request, user)

                if request.GET.get('next'):
                    return HttpResponsePermanentRedirect(request.GET.get('next'))

                return HttpResponsePermanentRedirect(reverse('index'))
             
            return render(request, 'auth_app/login.html', {'form':form, 'error':"Invalid Credentials!"})

        return render(request, 'auth_app/login.html', {'form':form})

    return render(request, 'auth_app/login.html', {'form':form})

def user_register(request):
    # return HttpResponse('Register Page')
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'auth_app/register.html', {'form':form})

@login_required()
def accounts_view(request):
    user_id = request.user.id
    user = UserModel.objects.get(id=user_id)
    # print(user.date_joined)
    return render(request, "auth_app/accounts.html", {'user_data':user})
    # NOTE: work pending on changing passwords accounts page!
    # NOTE: work pending on updating informations of an user accounts page!

@login_required()
def update_info_view(request):
    user_id = request.user.id
    user = UserModel.objects.get(id=user_id)
    form = CustomUserChangeForm(instance=user)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('account'))
        return render(request, 'auth_app/update.html',{"form":form})
    return render(request, 'auth_app/update.html', {"form":form})


def user_logout(request):
    logout(request)
    return HttpResponsePermanentRedirect(reverse('index'))


def del_user(request):
    user_id = request.user.id
    UserModel.objects.get(id=user_id).delete()
    return HttpResponsePermanentRedirect(reverse('login'))




# ::Note Section::
# NOTE: #1 Changing of password feature is pending for implementation.