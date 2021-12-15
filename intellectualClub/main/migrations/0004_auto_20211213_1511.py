# Generated by Django 2.2.25 on 2021-12-13 12:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211101_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='type',
        ),
        migrations.AddField(
            model_name='event',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='event',
            name='photo',
            field=models.ImageField(default=123, upload_to='photos/%Y/%n/%d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 13, 12, 11, 49, 86247, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='time_upload',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Тип')),
                ('event', models.ManyToManyField(related_name='event', to='main.Event', verbose_name='Тип события')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
    ]
