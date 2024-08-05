from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from Users.forms import ApplicationForm


# Create your views here.

#class ProfileUser(View):

class Application(View):
    def get(self, request):
        form = ApplicationForm
        data = {'form': form}
        return render(request, 'users/application.html', data)
    def post(self, request):
        return render(request, 'news/main.html')