from asgiref.sync import sync_to_async
from django.core.paginator import Paginator

from NEWS.models import News, Galery_Image_in_News


# @sync_to_async
# def news():
#     return News.objects.all()

async def get_news_on_main_page(): # временная функция при тестировании быстродействия сайта, исходя из результата будет известно нужна ли она,
    news = News.objects.filter(accepted=True).order_by('-time_updated')[:3]
    #news = News.objects.all()
    news_list = []
    async for new in news:
        news_list.append(new)
    return news_list

async def get_all_news():
    news = News.objects.filter(accepted=True).order_by('-time_updated')
    #news = News.objects.all()
    news_list = []
    async for new in news:
        news_list.append(new)
    return news_list

@sync_to_async
def get_news_information(id):
    return News.objects.get(id=id)



async def get_galery_news_image(id):
    galery = Galery_Image_in_News.objects.filter(news=id)
    galery_list = []
    async for image in galery:
        galery_list.append(image)
    return galery_list


@sync_to_async
def form_save(form):
    return form.save()

@sync_to_async
def get_user_is_authenticated(request):
    return request.user.is_authenticated

@sync_to_async
def get_pagination(request, news):
    paginator = Paginator(news, 3)          # Показывать по 3 объектов на странице
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)