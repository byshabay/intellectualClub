# Generated by Django 4.0.3 on 2022-05-06 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_category_name_en_category_name_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_fr',
            field=models.CharField(db_index=True, max_length=100, null=True, verbose_name='Название категории'),
        ),
        migrations.AddField(
            model_name='event',
            name='description_fr',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='event',
            name='short_description_fr',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='event',
            name='title_fr',
            field=models.CharField(max_length=50, null=True, verbose_name='Название'),
        ),
    ]
