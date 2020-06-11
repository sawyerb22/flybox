from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


RAINBOW_TROUT = 'Rainbow Trout'
BROWN_TROUT = 'Brown Trout'
BROOKE_TROUT = 'Brooke Trout'
TIGER_TROUT = 'Tiger Trout'
LAKE_TROUT = 'Lake Trout'
WHITE_FISH = 'White Fish'
GRAYLING = 'Grayling'

FISH_SPECIES = (
    (RAINBOW_TROUT, 'Rainbow Trout'),
    (BROWN_TROUT, 'Brown Trout'),
    (BROOKE_TROUT, 'Brooke Trout'),
    (TIGER_TROUT, 'Tiger Trout'),
    (LAKE_TROUT, 'Lake Trout'),
    (WHITE_FISH, 'White Fish'),
    (GRAYLING, 'Grayling')
)


class Fish(models.Model):
    species = models.CharField(
        choices=FISH_SPECIES, default=RAINBOW_TROUT, max_length=50)
    length = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    hole = models.ForeignKey(
        "river.Hole", related_name="hole_caught", on_delete=models.CASCADE)
    fly = models.OneToOneField("fly.Fly", null=True, on_delete=models.SET_NULL)
    # ForeignKey set on system.Image

    def __str__(self):
        return f"{self.type}"
