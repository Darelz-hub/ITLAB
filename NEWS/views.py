import requests
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import View
from NEWS.models import Video, News
from NEWS.asyns_news_function import get_all_news, get_news_on_main_page, get_news_information, get_galery_news_image, \
    get_user_is_authenticated, get_pagination
from asgiref.sync import sync_to_async

# Create your views here.
class MainPage(View):
    async def get(self, request):
        template_name = 'news/main.html'
        news = await get_news_on_main_page()
        is_authenticated = await get_user_is_authenticated(request)
        data = {'is_authenticated': is_authenticated, 'news': news}
        return render(request, template_name, data)

class PageNews(View):
    async def get(self, request):
        template_name = 'news/news.html'
        news = await get_all_news()
        page_obj = await get_pagination(request, news)
        is_authenticated = await get_user_is_authenticated(request)
        data = {'is_authenticated': is_authenticated, 'page_obj': page_obj}
        return render(request, template_name, data)

class NewsInformation(View):
    async def get(self, request, id):
        template_name = 'news/news_information.html'
        news = await get_news_information(id)
        galery = await get_galery_news_image(id)
        is_authenticated = await get_user_is_authenticated(request)
        data = {"news": news, 'galery': galery, 'is_authenticated': is_authenticated}
        return render(request,  template_name, data)