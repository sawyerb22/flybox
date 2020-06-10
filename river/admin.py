from django.contrib import admin
from . import models


@admin.register(models.River)
class RiverAdmin(admin.ModelAdmin):
    """Admin for rivers."""


@admin.register(models.Hole)
class HoleAdmin(admin.ModelAdmin):
    """Admin for Holes."""
