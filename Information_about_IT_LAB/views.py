from django.shortcuts import render
from django.views import View
import requests

from Information_about_IT_LAB.async_information_about_IT_LAB_function import get_documents, get_category_id
from NEWS.asyns_news_function import get_user_is_authenticated


# Create your views here.
class BasicInformation(View): # страница о Сведениях об образовательной организации
    async def get(self, request):
        template_name = 'information/basic_information.html'
        is_authenticated = await get_user_is_authenticated(request)
        data = {'is_authenticated': is_authenticated}
        return render(request, template_name, data)


class MainDocumentsPage(View):
    async def get(self, request):
        template_name = 'information/main_documents_page.html'
        is_authenticated = await get_user_is_authenticated(request)
        category_id = await get_category_id(name='MainDocuments')
        documents = await get_documents(category_id)
        data = {'documents': documents, 'is_authenticated': is_authenticated}
        return render(request, template_name, data)
