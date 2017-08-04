# django modules
from django.db import models

from .province import Province
from .infrastructure import Building


class Effect(models.Model):
    """ The core component of province change """

    """ e.g. Peasant Growth - would signify that applying this effect,
    with a given magnitude would impact how fast peasants grow per turn."""
    name = models.CharField(max_length=40,unique=False)

    """ Code used to identify the effect, like a key. """
    tag = models.CharField(max_length=40,unique=True)

    # others to be implemented

    def __str__(self):
        return self.name


class EffectInstance(models.Model):
    """ An instance of an effect that can be applied to a building or spell. """

    """ The related effect """
    effect = models.ForeignKey(Effect,
        on_delete=models.CASCADE,
        null=False,
        blank=False)

    """ Size of the effect. """
    magnitude = models.FloatField(default=0.0)


    def __str__(self):
        return "{} with mag. {}".format(self.effect.name, self.magnitude)


class EffectApplication(models.Model):
    """ Used to apply effects to provinces """
    instance = models.ForeignKey(EffectInstance,
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    province = models.ForeignKey(Province,
        on_delete=models.CASCADE,
        null=False,
        blank=False)

    """ Type of effect; alters how the effect is applied. """
    EFFECT_TYPE_CHOICES = (
        (1, 'immediate'),
        (2, 'each_round'),
        (3, 'one_round'),
        (4, 'on_expire'),
        (5, 'permanent'),
    )
    etype = models.IntegerField(choices=EFFECT_TYPE_CHOICES, default=1)

    # Round the effect was applied
    applied_on = models.IntegerField()
    # Round the effect expires (NULL permanent)
    expires_at = models.IntegerField()
