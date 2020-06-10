from django.contrib import admin
from system.models import Image
from . import models


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(models.River)
class RiverAdmin(admin.ModelAdmin):
    """Admin for rivers."""


@admin.register(models.Hole)
class HoleAdmin(admin.ModelAdmin):
    """Admin for Holes."""
    inlines = [
        ImageInline
    ]
