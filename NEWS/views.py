import requests
from django.shortcuts import render, get_object_or_404
from django.views import View
from NEWS.models import Video

# Create your views here.
class MainPage(View):
    def get(self, request):
        #return render(request, 'news/main.html')
        # video = get_object_or_404(Video, title='ITLAB')
        # data = {'video': video}
        # print(video.title)
        return render(request, 'news/main.html')