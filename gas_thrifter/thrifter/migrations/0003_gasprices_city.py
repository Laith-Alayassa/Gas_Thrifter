# Generated by Django 3.2.13 on 2022-06-08 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thrifter', '0002_cities'),
    ]

    operations = [
        migrations.AddField(
            model_name='gasprices',
            name='city',
            field=models.ForeignKey(default= 999999, on_delete=django.db.models.deletion.CASCADE, to='thrifter.cities'),
        ),
    ]