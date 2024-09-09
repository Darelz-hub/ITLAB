from asgiref.sync import sync_to_async

from NEWS.models import News


# @sync_to_async
# def news():
#     return News.objects.all()

async def get_news():
    news = News.objects.filter(accepted=True).order_by('-time_updated')[:3]
    #news = News.objects.all()
    news_list = []
    async for new in news:
        news_list.append(new)
    return news_list