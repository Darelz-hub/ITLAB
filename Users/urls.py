
from .forms import LoginFormUser
from . import views

from django.urls import path

from django.contrib.auth.views import (LoginView, LogoutView)


app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html',
                                     authentication_form=LoginFormUser), name='login'), # переход на профиль
    path('logout/', LogoutView.as_view(), name='logout'), # выход
    #path('profile/', views.ProfileUser.as_view(), name='profile')
]
