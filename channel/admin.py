from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models



@admin.register(models.ChannelType)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.ChannelImg)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "get_thumbnail","file","channel")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"


@admin.register(models.Channel)
class ChannelAdmin(admin.ModelAdmin):
    fieldsets = (
        (
        "Basic Info",
          {
              "fields":(
              "name",
              "link",
              "description",
              "channeltype",

          )
        },
     ),

)

    list_display = (

        "name",
        "link",
        "description",
        "channeltype",



    )

