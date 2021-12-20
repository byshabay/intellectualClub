# Generated by Django 2.2.25 on 2021-12-20 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20211215_2330'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-time_create', 'title'], 'verbose_name': 'Событие', 'verbose_name_plural': 'События'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='event',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='event',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%n/%d', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='event',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='event',
            name='time_upload',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
    ]