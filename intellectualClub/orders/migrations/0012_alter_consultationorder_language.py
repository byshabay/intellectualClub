# Generated by Django 4.0.3 on 2022-05-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_consultationorder_created_consultationorder_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultationorder',
            name='language',
            field=models.CharField(choices=[('EN', 'English'), ('FR', 'French'), ('RUS', 'Russian')], default='EN', max_length=3),
        ),
    ]