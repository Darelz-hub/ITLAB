from asgiref.sync import sync_to_async

from NEWS.models import News


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
