# django modules
from django.db import models
from django.urls import reverse

from django.core.validators import MaxValueValidator, MinValueValidator

class Spell(models.Model):
    """ Object that applies it's linked effect to a province based on the
    percentage built within an infrastructure """

    """ Unique name of building """
    name = models.CharField(max_length=40, unique=True)

    """ A human readable description of what the building does """
    description = models.CharField(max_length=200)

    """ The range in which this spell can variable from the given
    EffectInstance amount. If this number is 0 it cannot vary. If the number is
    20, then the final amount can be 20 percent smaller or larger."""
    variable_range = models.IntegerField(default=0)

    """ The difficulty of the Spell. The higher the number, the more of an
    advantage in magical strength is required. """
    difficulty = models.FloatField(
        validators = [MinValueValidator(0.0), MaxValueValidator(1.0)]
    )

    effect_instance = models.ManyToManyField('EffectInstance')

    def __str__(self):
        return self.name
