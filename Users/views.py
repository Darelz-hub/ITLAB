from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from Users.forms import ApplicationForm


# Create your views here.

#class ProfileUser(View):

class Application(FormView): # форма заявки
    template_name = 'users/application.html'
    form_class = ApplicationForm
    success_url = '/'
    def form_valid(self, form): # метод для сохранения данных в бд
        form.save()
        return super().form_valid(form)
