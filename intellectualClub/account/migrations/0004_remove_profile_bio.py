# Generated by Django 4.0.3 on 2022-04-03 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
    ]