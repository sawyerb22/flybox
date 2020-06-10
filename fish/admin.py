from django.contrib import admin
from . import models
from system.models import Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(models.Fish)
class FishAdmin(admin.ModelAdmin):
    """Admin for fish."""
    inlines = [
        ImageInline
    ]
