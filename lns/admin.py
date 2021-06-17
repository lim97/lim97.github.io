from django.contrib import admin
from . import models

@admin.register(models.Question)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "date",
    )
