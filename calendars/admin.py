from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models

@admin.register(models.Calendars)
class CalendarsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "subname",
        "date",
        "description",
    )
@admin.register(models.CalenImg)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "get_thumbnail","file","calen")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
