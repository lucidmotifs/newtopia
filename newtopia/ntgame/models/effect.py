# django modules
from django.db import models


class Effect(models.Model):
    """ The core component of province change """

    """ e.g. Peasant Growth - would signify that applying this effect,
    with a given magnitude would impact how fast peasants grow per turn."""
    name = models.CharField(max_length=40,unique=True)

    """ Code used to identify the effect, like a key. """
    tag = models.CharField(max_length=40,unique=True)

    """ Type of effect; alters when the effect is applied. """
    EFFECT_TYPE_CHOICES = (
        (1, 'immediate'),
        (2, 'each_round'),
        (3, 'one_round'),
        (4, 'on_expire'),
        (5, 'permanent'),
    )
    etype = models.IntegerField(choices=EFFECT_TYPE_CHOICES, default=1)

    # others to be implemented
    '''
    expires_at (ntdate)
    applies_at (ntate)
    '''

    def __str__(self):
        return self.name


class EffectInstance(models.Model):
    """ An instance of an effect that can be applied to a building or spell. """
    effect = ForeignKey(Effect,
        on_delete=models.CASCADE,
        null=False,
        blank=False)
