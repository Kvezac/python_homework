# Generated by Django 4.2.4 on 2023-08-27 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educatioanal_app', '0002_alter_work_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='work',
            options={'verbose_name': 'проект', 'verbose_name_plural': 'проекты'},
        ),
    ]