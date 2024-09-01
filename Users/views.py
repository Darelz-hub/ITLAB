from asgiref.sync import sync_to_async
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from Users.forms import ApplicationForm
from Users.models import Profile
from django.http import JsonResponse

from Users.users_function import get_user_profile, change_profile_user, get_secions


# Create your views here.


# async def alogin(request, user, backend=None):
#
#     return await sync_to_async(login)(request, user, backend)

class ProfileUser(View):
     async def get(self, request):
        user = await request.auser()
        profile = await get_user_profile(user)
        secions = await get_secions(profile)
        data = {'user': user, 'profile': profile, 'secions': secions}
        template_name = 'users/profile.html'
        return render(request, template_name, data)
class ProfileChange(View):
    async def post(self, request):
        email = request.POST.get('email')
        quote = request.POST.get('quote')
        await change_profile_user(request, email, quote)
        return JsonResponse({'message': 'Профиль изменён'})

class Application(FormView): # форма заявки
    template_name = 'users/application.html'
    form_class = ApplicationForm
    success_url = '/'
    def form_valid(self, form): # метод для сохранения данных в бд
        form.save()
        return super().form_valid(form)
