# Generated by Django 4.0.3 on 2022-03-31 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='photos/profile_pic/', verbose_name='Изображение'),
        ),
    ]
