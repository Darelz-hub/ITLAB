from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm

from Users.models import ApplicationUsers


class LoginFormUser(AuthenticationForm): # форма авторизации
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class ApplicationForm(ModelForm):
    def __init__(self, *args, **kwargs): # убираем у всех полей input label
        super(ModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''
    class Meta:
        model = ApplicationUsers
        fields = ['group', 'full_name', 'sections', 'telegram', 'descriptions']
        widgets = {
                'group': forms.TextInput(attrs={'placeholder': 'Группа'}),
                'full_name': forms.TextInput(attrs={'placeholder': 'ФИО'}),
                'telegram': forms.TextInput(attrs={'placeholder': 'Телеграм'}),
                'descriptions': forms.TextInput(attrs={'placeholder': 'Информация о вас'})
        }

# class ProfileUser(ModelForm):
#     username = forms.CharField