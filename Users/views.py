from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from Users.forms import ApplicationForm


# Create your views here.

#class ProfileUser(View):

class Application(View):
    def get(self, request):
        form_class = ApplicationForm
        template = 'users/application.html'
        render(request, template_name=template)