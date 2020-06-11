from django.db import models
import graphene
from graphene import Field, Int, List, String
from graphene_django import DjangoObjectType

from ..models import Fish
from system.models import Image
from system.graphql.types import ImageType


class FishType(DjangoObjectType):
    fish_images = List(ImageType)

    class Meta:
        model = Fish
        only_fields = [
            "id",
            "species",
            "length",
            "weight",
            "hole",
            "fly"
        ]

    def resolve_fish_images(self, info):
        return Image.objects.filter(fish=self)
