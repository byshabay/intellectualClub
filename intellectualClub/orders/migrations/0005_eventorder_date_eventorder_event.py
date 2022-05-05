# Generated by Django 4.0.3 on 2022-05-05 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_event_author'),
        ('orders', '0004_rename_order_eventorder_delete_eventinorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventorder',
            name='date',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='main.eventschedule'),
        ),
        migrations.AddField(
            model_name='eventorder',
            name='event',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='main.event'),
        ),
    ]
