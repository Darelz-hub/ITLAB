from django.db import models
from django.core.validators import FileExtensionValidator

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