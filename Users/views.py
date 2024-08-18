from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from Users.forms import ApplicationForm
from Users.models import Profile
from django.http import JsonResponse

# Create your views here.

class ProfileUser(View):
    def get(self, request):
        template_name = 'users/profile.html'
        return render(request, template_name)
class ProfileChange(View):
    def post(self, request):
        email = request.POST.get('email')
        user = User.objects.get(id=request.user.id)
        user.email = email
        user.save()
        return JsonResponse({'message': 'Профиль изменён'})

class Application(FormView): # форма заявки
    template_name = 'users/application.html'
    form_class = ApplicationForm
    success_url = '/'
    def form_valid(self, form): # метод для сохранения данных в бд
        form.save()
        return super().form_valid(form)
