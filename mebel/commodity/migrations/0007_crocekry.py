# Generated by Django 3.2 on 2022-04-06 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0006_alter_product_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crocekry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('photo', models.ImageField(upload_to='')),
                ('prise', models.CharField(max_length=20)),
                ('desciption', models.CharField(max_length=10000)),
            ],
        ),
    ]
