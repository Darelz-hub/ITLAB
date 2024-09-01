import requests
from django.shortcuts import render, get_object_or_404
from django.views import View
from NEWS.models import Video, News
from NEWS.news_function import get_news
from asgiref.sync import sync_to_async

# Create your views here.
class MainPage(View):
    async def get(self, request):
        template_name = 'news/main.html'
        user = await request.auser()
        news = await get_news()
        is_authenticated = user.is_authenticated
        data = {'is_authenticated': is_authenticated, 'news': news}
        return render(request, template_name, data)

