# Generated by Django 4.0.3 on 2022-05-13 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_status_name_en_status_name_fr_status_name_ru'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventorder',
            name='date',
        ),
    ]
