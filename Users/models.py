from django.db import models

# Create your models here.

class Secions(models.Model):
    name = models.CharField(verbose_name='Наименование')
    name_ru = models.CharField(verbose_name='Наименование на русском')

class ApplicationUsers(models.Model):
    group = models.CharField(max_length=20, verbose_name='Группа')
    full_name = models.CharField(max_length=30, verbose_name='ФИО')
    sections = models.ForeignKey(Secions, related_name='sections', on_delete=models.CASCADE, verbose_name='Секция')
    telegram = models.CharField(max_length=100, verbose_name='Ваш телеграмм')
    descriptions = models.TextField(max_length=1000,verbose_name='Информация о вас')