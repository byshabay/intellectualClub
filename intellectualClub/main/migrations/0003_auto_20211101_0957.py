# Generated by Django 3.2.8 on 2021-11-01 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_even_event'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Событие', 'verbose_name_plural': 'События'},
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.CharField(default='', max_length=50, verbose_name='Тип'),
        ),
    ]
