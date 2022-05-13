# Generated by Django 4.0.3 on 2022-05-13 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_categorymetadata_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupOfMetaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='categorymetadata',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.groupofmetadata'),
        ),
    ]
