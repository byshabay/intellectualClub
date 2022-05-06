# Generated by Django 4.0.3 on 2022-05-06 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_event_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='short_description_en',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='event',
            name='short_description_ru',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='event',
            name='title_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='event',
            name='title_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Название'),
        ),
    ]