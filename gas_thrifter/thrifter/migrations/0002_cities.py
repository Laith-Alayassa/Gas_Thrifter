# Generated by Django 3.2.13 on 2022-06-08 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thrifter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, unique=b'I01\n')),
            ],
        ),
    ]
