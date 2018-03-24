# python modules
from enum import Enum

# django modules
from django.db import models

# nt modules
from .province import Province
from .infrastructure import Building


class Effect(models.Model):
    """ The core component of province change """

    """ e.g. Peasant Growth - would signify that applying this effect,
    with a given magnitude would impact how fast peasants grow per turn."""
    name = models.CharField(max_length=40,unique=False)

    """ The entity that generated the effect """
    entity = models.ForeignKey('ntmeta.Entity',
        on_delete=models.CASCADE,
        null=False,
        blank=False)

    """ Code used to identify the effect, like a key. HASH? """
    tag = models.CharField(max_length=40,unique=True)

    def __str__(self):
        return self.name


class EffectInstance(models.Model):
    """ An instance of an effect that can be applied to a building or spell. """

    class EffectType(Enum):
        DELAYED = 1
        IMMEDIATE = 2     
        OVER_TIME = 3
        NEXT_TURN = 4

    """ The related effect """
    effect = models.ForeignKey(Effect,
        on_delete=models.CASCADE,
        null=False,
        blank=False)

    """ Determines the type of application produced """
    effect_type = models.IntegerField(
        choices=[e.value for e in EffectType], default=EffectType.IMMEDIATE)

    """ How long effect persists. Ignore when `effect_type` is immediate and
        determines when the delayed effect pops when `effect_type` is
        DELAYED. Measured in ntdays """
    duration = models.IntegerField(deault=1)

    """ Size of the effect. Set to 100 if using raw value. """
    magnitude = models.FloatField(default=0.0)

    """ Raw value increase/decrease will be converted to a percentage
        if used with a subentity, such as a growth rate.
        When Provided, magnitude will only be applied to the raw_value.
        Exception: can be used as minimum value if base_is_min == True """
    base_value = models.IntegerField(default=None)

    """ When True, magnitude works as usual, and base_value is only applied if
        the resulting Application value would be less than the base_value """
    base_is_min = models.BooleanField(defaul=False)

    """ Denotes negative or positive version of effect """
    is_negative = models.BooleanField(default=False)


    def apply(self, province):
        app = EffectApplication()
        app.instance = self
        app.province = province
        app.


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

    applied_by = models.ForeignKey(Province,
        on_delete=models.CASCADE,
        null=False,
        blank=False)

    """ Type of effect; alters how the effect is applied. """
    # Round the effect was applied (ntdate)
    applied_on = models.IntegerField()
    # Round the effect expires (ntdate) (NULL permanent, immediate)
    expires_at = models.IntegerField(default=None)
    # Round the effect is applied (ntdate)
    # (NULL immediate, 0 every tick till expires)
    applies_at = models.IntegerField(default=None)
