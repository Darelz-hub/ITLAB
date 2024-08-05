from django.urls import path, include
import NEWS.views as news

app_name = 'news'
urlpatterns = [
    path('', news.MainPage.as_view(), name='main')
]