from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from fish.models import Fish


class River(models.Model):
    location = models.CharField(max_length=1000)
    title = models.CharField(max_length=150, blank=False)
    image = ProcessedImageField(
        upload_to="user_photos",
        format="JPEG",
        options={"quality": 90},
        processors=[ResizeToFit(width=1200, height=1200)],
    )
    time_of_year = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Hole(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=1000)
    time_of_year = models.DateField(auto_now_add=True)
    water_level = models.CharField(max_length=5)
    water_temperature = models.CharField(max_length=3)
    river = models.ForeignKey(
        River, related_name="river_hole", on_delete=models.CASCADE)
    flies = models.ManyToManyField(
        "fly.Fly", related_name="flies_used")

    # ForeignKey on system.Image

    def __str__(self):
        return f"{self.title}"
