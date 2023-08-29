from email.mime import image

from django.db import models


class Work(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='фото', upload_to='educational_app/images')
    project_file = models.FileField(verbose_name='файл проекта', upload_to='educational_app/docments')
    created = models.DateTimeField(verbose_name='дата', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = "проекты"
