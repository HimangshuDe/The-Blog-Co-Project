from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

from auth_app.models import UserModel

# Custom UserCreationForm and UserChangeForm


# For adding a new user through admin site
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput({'placeholder':'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput({'placeholder':'Last Name'}))
    class Meta:
        model = UserModel
        fields = ["first_name", "last_name","email"]
        widgets = {
            'email':forms.TextInput(attrs={'placeholder':'Email'})
        }
        
    
    def __init__(self, *args, **kwargs) :
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder':'Confirm Password'})


# For updating or changing a user through admin site.
class CustomUserChangeForm(UserChangeForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
        attrs={'placeholder':'DD-MM-YYYY', 'type':'date'},
        format="DD-MM-YYY",
    ))
    class Meta:
        model = UserModel
        exclude = ['user_permissions', 'groups', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'date_joined']
        

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()



class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput({"placeholder":"Email"}), error_messages={"required":"Email is required"})
    password = forms.CharField(widget=forms.PasswordInput({"placeholder":"Password"}), error_messages={"required":"Can't login without a Password!"})


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Enter Old Password', widget=forms.PasswordInput(attrs={"placeholder":"Old Password"}),error_messages={"required":"This is required"})
    
    new_password1 = forms.CharField(label="Enter new password", widget=forms.PasswordInput(attrs={"placeholder":"New Password"}))

    new_password2 = forms.CharField(label="Retype that", widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))