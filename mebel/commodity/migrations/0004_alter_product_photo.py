# Generated by Django 3.2 on 2022-04-04 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0003_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(null=True, upload_to='product'),
        ),
    ]
