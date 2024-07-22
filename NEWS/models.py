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