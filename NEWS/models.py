from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название на английском')
    title_ru = models.CharField(max_length=100, verbose_name='Название на русском')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='image/', verbose_name='Изображение')
    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
        verbose_name='Видео'
    )
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

class News(models.Model):
    # title = models.CharField(max_length=100, verbose_name='Название на английском')
    title = models.CharField(max_length=100,verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    brief_description = models.CharField(max_length=100, verbose_name='Краткое описание')
    main_image = models.ImageField(upload_to='image/', verbose_name='Главное изображение')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    accepted = models.BooleanField(default=False, verbose_name='Одобрено')

    def __str__(self):
        return self.title
class Galery_News(models.Model):
    image = models.ImageField(upload_to='gallery')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')