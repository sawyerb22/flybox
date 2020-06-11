import graphene
from django.db import models
from graphene import Field, List, Int, ID, NonNull, ObjectType
from graphene_django import DjangoObjectType
from ..models import Fish
from .types import FishType


class GetAllFishQuery(ObjectType):
    all_fish = NonNull(List(FishType))

    def resolve_all_fish(self, info):
        return Fish.objects.all()


class GetUniqueFishQuery(ObjectType):
    fish = Field(FishType, fish_id=ID())

    def resolve_fish(self, info, fish_id):
        fish = Fish.objects.get(id=fish_id)
        return fish


class GetHoleFishQuery(ObjectType):
    fish_from_hole = List(FishType, hole_id=ID())

    def resolve_fish_from_hole(self, info, hole_id):
        fish_from_hole = Fish.objects.filter(hole=hole_id)
        return fish_from_hole
