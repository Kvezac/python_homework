# Generated by Django 4.2.4 on 2023-08-21 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(upload_to='educational_app/images'),
        ),
    ]
