# Generated by Django 3.2.13 on 2022-06-09 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thrifter', '0005_auto_20220609_0407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cities',
            name='address',
        ),
        migrations.AddField(
            model_name='gasprices',
            name='address',
            field=models.CharField(default='NA', max_length=100),
        ),
    ]
