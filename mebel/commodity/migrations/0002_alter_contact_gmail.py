# Generated by Django 3.2 on 2022-03-27 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='gmail',
            field=models.EmailField(max_length=254),
        ),
    ]