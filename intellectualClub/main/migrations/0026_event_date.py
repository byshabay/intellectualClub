# Generated by Django 4.0.3 on 2022-05-13 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_groupofmetadata_alter_categorymetadata_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]