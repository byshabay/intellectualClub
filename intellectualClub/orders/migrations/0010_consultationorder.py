# Generated by Django 4.0.3 on 2022-05-13 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_remove_eventorder_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultationOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_email', models.CharField(max_length=255)),
                ('customer_phone', models.CharField(max_length=255)),
                ('customer_name', models.CharField(max_length=255)),
                ('language', models.CharField(choices=[('EN', 'English'), ('FR', 'French'), ('RUS', 'Russian'), ('GER', 'German')], default='EN', max_length=3)),
                ('comment', models.TextField()),
            ],
        ),
    ]