from django.db import models
from fly.models import Fly


class FlyBox(models.Model):
    title = models.CharField(max_length=150)
    fly = models.ManyToManyField(Fly, related_name="fly")

    def __str__(self):
        return f"{self.title}"
