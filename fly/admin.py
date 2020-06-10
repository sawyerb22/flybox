from django.contrib import admin
from . import models


@admin.register(models.Fly)
class FlyAdmin(admin.ModelAdmin):
    """Admin for flies."""
