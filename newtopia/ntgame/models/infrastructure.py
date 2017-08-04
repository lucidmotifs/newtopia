# django modules
from django.db import models
from django.urls import reverse

# ntgame models
from .province import Province


class Building(models.Model):
    """ Object that applies it's linked effect to a province based on the
    percentage built within an infrastructure """

    """ Unique name of building """
    name = models.CharField(max_length=40, unique=True)

    """ A human readable description of what the building does """
    description = models.CharField(max_length=200)

    """ The rate at which the effectiveness of the building diminishes. The
    higher this number the less effective building higher quantities of
    the building would be. """
    diminishing_return = models.FloatField()

    effect_instance = models.ManyToManyField('EffectInstance')

    def effect_instances(self):
        """ Return a string of EffectInstances attached to this Object """
        return ", ".join([e.effect.name for e in self.effect_instance.all()])

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
