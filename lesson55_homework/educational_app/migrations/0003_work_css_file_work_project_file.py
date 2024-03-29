# Generated by Django 4.2.4 on 2023-08-24 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_app', '0002_alter_work_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='css_file',
            field=models.FileField(default='', null=True, upload_to='educational_app/css'),
        ),
        migrations.AddField(
            model_name='work',
            name='project_file',
            field=models.FileField(default='', upload_to='educational_app/documents'),
            preserve_default=False,
        ),
    ]
