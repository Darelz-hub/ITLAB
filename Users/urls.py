
from .forms import LoginFormUser
import Users.views as users
from django.urls import path, reverse_lazy

from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetView, PasswordResetDoneView,
                                       PasswordResetConfirmView, PasswordResetCompleteView)
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html',
                                     authentication_form=LoginFormUser), name='login'), # переход на профиль
    path('logout/', LogoutView.as_view(), name='logout'), # выход
    path('password-reset/', PasswordResetView.as_view(
        template_name='users/password_reset_form.html',
        success_url=reverse_lazy('users:password_reset_done'),
        email_template_name='users/password_reset_email.html'
    ), name='password_reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html',
        success_url=reverse_lazy('users:password_reset_complete')
    ), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'
    ), name='password_reset_complete'),
    path('application/', users.Application.as_view(), name='application'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('profile_change/', views.ProfileChange.as_view(), name='profile_change'),
]
