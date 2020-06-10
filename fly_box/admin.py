from django.contrib import admin

from . import models


@admin.register(models.FlyBox)
class FlyBoxAdmin(admin.ModelAdmin):
    """Admin for fly boxes."""
