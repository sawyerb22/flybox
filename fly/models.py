from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from fish.models import Fish
from river.models import River


class Fly(models.Model):

    NYMPH = 'Nymph'
    EMERGER = "Emerger"
    DRY = 'Dry'
    STREAMER = 'Streamer'
    WET = 'Wet'

    FLY_TYPES = (
        (NYMPH, 'Nymph'),
        (EMERGER, 'Emerger'),
        (DRY, 'Dry'),
        (STREAMER, 'Streamer'),
        (WET, 'Wet')
    )

    type = models.CharField(
        choices=FLY_TYPES, default=NYMPH, max_length=10)
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=4)
    image = ProcessedImageField(
        upload_to="user_photos",
        format="JPEG",
        options={"quality": 90},
        processors=[ResizeToFit(width=1200, height=1200)]
    )
    description = models.CharField(max_length=350)
    time_of_year = models.DateField(auto_now_add=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.name}"
