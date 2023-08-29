from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Work


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_description', 'get_image', 'project_file', 'created')
    list_filter = ('created',)

    def get_description(self, obj):
        return obj.description[90]
    get_description.short_description = 'описание'

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100", height="90"')

    get_image.short_description = 'Изображение'




