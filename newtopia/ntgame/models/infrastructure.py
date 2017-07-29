# django modules
from django.db import models
from django.urls import reverse

# ntgame models
from .effect import Effect
from .province import Province


class Building(models.Model):
    """ Object that applies it's linked effect to a province based on the
    percentage built within an infrastructure """

    name = models.CharField(max_length=40)

    description = models.CharField(max_length=200)

    magnitude = models.IntegerField()

    """ The rate at which the effectiveness of the building diminishes. The
    higher this number the less effective building higher quantities of
    the building would be. """
    diminishing_ratio = models.FloatField()

    effect = models.ManyToManyField(Effect)

    def __str__(self):
        return self.name


class Infrastructure(models.Model):
    """ Stores the basic data for a Province's infrastructure """

    land = models.IntegerField(default=400)

    explored = models.IntegerField(default=0)

    built = models.IntegerField(default=0)

    province = models.OneToOneField(Province,
        parent_link=True,
        primary_key=False,
        on_delete=models.CASCADE)


class InfrastructureItem(models.Model):
    """ Links a building to an infrastructure with a given amount """

    building = models.ForeignKey(Building,
        on_delete=models.CASCADE,
        null=False,
        blank=False)

    number = models.IntegerField()

    infrastructure = models.ForeignKey(Infrastructure,
        on_delete=models.CASCADE,
        null=False,
        blank=False)
