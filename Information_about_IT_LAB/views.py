from django.shortcuts import render
from django.views import View
import requests

from NEWS.asyns_news_function import get_user_is_authenticated


# Create your views here.
class BasicInformation(View): # страница о Сведениях об образовательной организации
    async def get(self, request):
        template_name = 'information/basic_information.html'
        is_authenticated = await get_user_is_authenticated(request)
        data = {'is_authenticated': is_authenticated}
        return render(request, template_name, data)



