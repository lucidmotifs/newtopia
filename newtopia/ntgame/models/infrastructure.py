# django modules
from django.db import models

# ntgame models
from .effect import Effect


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

    land = models.IntegerField()

    explored = models.IntegerField()

    built = models.IntegerField()


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
