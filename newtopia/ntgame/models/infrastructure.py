# django modules
from django.db import models
from django.urls import reverse

# ntgame models
from .effect import Effect
from .province import Province


class Building(models.Model):

    name = models.CharField(max_length=40)

    description = models.CharField(max_length=40)

    magnitude = models.IntegerField()

    diminishing_ratio = models.FloatField()

    effect = models.ForeignKey(Effect,
        on_delete=models.CASCADE,
        null=True,
        blank=True)


class Infrastructure(models.Model):

    land = models.IntegerField(default=400)

    explored = models.IntegerField(default=0)

    built = models.IntegerField(default=0)

    province = models.OneToOneField(Province,
        parent_link=True,
        primary_key=False,
        on_delete=models.CASCADE)


class InfrastructureItem(models.Model):

    building = models.ForeignKey(Building,
        on_delete=models.CASCADE,
        null=False,
        blank=False)

    number = models.IntegerField()

    infrastructure = models.ForeignKey(Infrastructure,
        on_delete=models.CASCADE,
        null=False,
        blank=False)
