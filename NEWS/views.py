import requests
from django.shortcuts import render, get_object_or_404
from django.views import View
from NEWS.models import Video

# Create your views here.
class MainPage(View):
    async def get(self, request):
        template = 'news/main.html'
        user = await request.auser()
        is_authenticated = user.is_authenticated
        data = {'is_authenticated': is_authenticated}
        return render(request, template, data)