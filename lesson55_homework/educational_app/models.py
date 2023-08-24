from django.db import models


class Work(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='educational_app/images')
    project_file = models.FileField(upload_to='educational_app/documents',  null = True, default='')
    css_file = models.FileField(upload_to='educational_app/css', null = True, blank=True, default='')

    def __str__(self):
        return self.title
