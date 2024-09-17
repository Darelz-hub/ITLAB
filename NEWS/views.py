import requests
from django.shortcuts import render, get_object_or_404
from django.views import View
from NEWS.models import Video, News
from NEWS.asyns_news_function import get_all_news, get_news_on_main_page, get_news_information
from asgiref.sync import sync_to_async

# Create your views here.
class MainPage(View):
    async def get(self, request):
        template_name = 'news/main.html'
        user = await request.auser()
        news = await get_news_on_main_page()
        is_authenticated = user.is_authenticated
        data = {'is_authenticated': is_authenticated, 'news': news}
        return render(request, template_name, data)

class PageNews(View):
    async def get(self, request):
        template_name = 'news/news.html'
        news = await get_all_news()
        data = {'news': news}
        return render(request, template_name, data)

class NewsInformation(View):
    async def get(self, request, id):
        template_name = 'news/news_information.html'
        news = await get_news_information(id)
        data = {"news": news}
        return render(request,  template_name, data)