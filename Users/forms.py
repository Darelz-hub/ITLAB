from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm


class LoginFormUser(AuthenticationForm): # форма авторизации
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


# class Application(ModelForm):
#

# class ProfileUser(ModelForm):
#     username = forms.CharField