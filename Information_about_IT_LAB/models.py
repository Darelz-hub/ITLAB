from django.db import models
from django.core.validators import FileExtensionValidator
from phone_field import PhoneField
# Create your models here.

class CategoryDocument(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    name_ru = models.CharField(max_length=255, verbose_name='Наименование на русском')
    def __str__(self):
        return self.name_ru
class Documents(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    document = models.FileField(
        upload_to='documents/', null=True, blank=True,
        validators=[FileExtensionValidator(['pdf', 'doc', 'docx', 'txt', 'xls', 'xlsx'])],
        verbose_name='Документ')
    category = models.ForeignKey(CategoryDocument, on_delete=models.CASCADE, verbose_name="секция",blank=True, null=True)

class ITLABRole(models.Model):
    title = models.CharField(max_length=255, verbose_name='роль в it lab')
    title_ru = models.CharField(max_length=255, verbose_name='роль на русском')
    def __str__(self):
        return self.title_ru
class Management(models.Model):
    role = models.ForeignKey(ITLABRole, on_delete=models.CASCADE, verbose_name="роль в IT LAB", blank=True, null=True)
    image = models.ImageField(upload_to='management/', blank=True, null=True, max_length=255,
                              validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif'])],
                              verbose_name='Фотография')
    fullName = models.CharField(max_length=255, verbose_name='ФИО')
    job_title = models.CharField(max_length=255, verbose_name='Должность в вузе', blank=True, null=True)
    phone = PhoneField(blank=True, null=True, help_text='Ваш номер телефона', verbose_name='Телефон')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')