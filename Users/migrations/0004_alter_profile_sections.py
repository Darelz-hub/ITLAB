# Generated by Django 5.0.6 on 2024-08-22 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_profile_sections_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sections',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.secions', verbose_name='секция'),
        ),
    ]
