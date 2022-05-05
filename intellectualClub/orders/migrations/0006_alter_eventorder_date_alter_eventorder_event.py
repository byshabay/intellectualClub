# Generated by Django 4.0.3 on 2022-05-05 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_event_author'),
        ('orders', '0005_eventorder_date_eventorder_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventorder',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.eventschedule'),
        ),
        migrations.AlterField(
            model_name='eventorder',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.event'),
        ),
    ]
