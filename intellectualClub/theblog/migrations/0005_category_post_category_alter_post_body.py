# Generated by Django 4.0.3 on 2022-04-27 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0004_post_post_date_alter_post_author_alter_post_body_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='test', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(verbose_name='Содержимое'),
        ),
    ]
