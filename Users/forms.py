from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model

class LoginFormUser(AuthenticationForm): # форма авторизации
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']