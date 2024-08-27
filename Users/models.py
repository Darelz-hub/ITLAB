from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Secions(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    name_ru = models.CharField(max_length=50, verbose_name='Наименование на русском')

    def __str__(self):
        return self.name_ru

class ApplicationUsers(models.Model):
    group = models.CharField(max_length=20, verbose_name='Группа')
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    sections = models.ForeignKey(Secions, related_name='sections', on_delete=models.CASCADE, verbose_name='Секция')
    telegram = models.CharField(max_length = 100, verbose_name='Ваш телеграмм')
    descriptions = models.TextField(max_length = 1000,verbose_name='Информация о вас')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    accepted = models.BooleanField(default=False, verbose_name='Одобрено')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField(upload_to='imagedb/', blank=True, null=True, max_length=255, validators=[
        FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif'])], verbose_name='Изображение')
    quote = models.CharField(blank=True, null=True, max_length=255, verbose_name='Любимая цитата')
    group = models.CharField(verbose_name='Группа', max_length=255, blank=True, null=True)
    sections = models.ForeignKey(Secions, on_delete=models.CASCADE, verbose_name="секция",blank=True, null=True)
    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профиль пользователя'

    #автоматически создаёт профиль пользователя при регистрации
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username