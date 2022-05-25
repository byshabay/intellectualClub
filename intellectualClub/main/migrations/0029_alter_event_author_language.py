# Generated by Django 4.0.3 on 2022-05-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_delete_consultationorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='author_language',
            field=models.CharField(choices=[('EN', 'English'), ('FR', 'French'), ('RUS', 'Russian')], default='RUS', max_length=3),
        ),
    ]
