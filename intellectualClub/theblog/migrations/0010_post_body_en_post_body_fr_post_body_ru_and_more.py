# Generated by Django 4.0.3 on 2022-05-11 11:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0009_post_header_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body_fr',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='snippet_en',
            field=models.CharField(default='Test', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='snippet_fr',
            field=models.CharField(default='Test', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='snippet_ru',
            field=models.CharField(default='Test', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_fr',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
    ]
