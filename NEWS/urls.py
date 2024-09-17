from django.urls import path, include
import NEWS.views as news

app_name = 'news'
urlpatterns = [
    path('', news.MainPage.as_view(), name='main'), # основная страница
    path('news/', news.PageNews.as_view(), name='page_news'), # получение станицы со всеми новостями
    path('news/<int:id>', news.NewsInformation.as_view(), name='news_information'), # получение информации о новости
]