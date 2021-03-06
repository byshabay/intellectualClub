# Generated by Django 4.0.3 on 2022-05-13 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_event_is_popular_event_is_promo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='short_description',
            field=models.CharField(default='Test', max_length=228),
        ),
        migrations.AlterField(
            model_name='event',
            name='short_description_en',
            field=models.CharField(default='Test', max_length=228, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='short_description_fr',
            field=models.CharField(default='Test', max_length=228, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='short_description_ru',
            field=models.CharField(default='Test', max_length=228, null=True),
        ),
        migrations.CreateModel(
            name='CategoryMetaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
    ]
