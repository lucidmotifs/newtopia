from enum import Enum

from django.db import models


class EntityGroup(models.Model):
    label = models.CharField(max_lenth=40, unique=True)
    # determines the Game Model that a relationship with the generated model
    # is formed i.e. Resource -> Province means that every resource is a
    # property of Province. NB. Should be choice field TODO
    related_model = models.CharField(max_length=100)
    generate = models.BooleanField()
    create_relationships = models.BooleanField()


class Entity(models.Model):
    """ Describes any tangible object and creates relationships via
        grouping to become a property of a Game model. """

    class EntityType(Enum):
        SIMPLE = 'SIMPLE'
        MODEL = 'MODEL'

    name = models.CharField(max_length=40, unique=True)
    group = models.ForeignKey(
        EntityGroup, on_delete=models.CASCADE, null=True)
    ttype = models.CharField(
        max_length=10, choices=(
            EntityType.SIMPLE, 'Simple', EntityType.MODEL, 'Model'))


class Aspect(models.Model):
    """ Aspects can be applied to Entities so their behaviour and
        effects can be inferred. They can be likened to 'meta-effects'.

        Note that Aspects related to Effects and not effect Instances, this is
        because the relationship has only one property - weight 
        (i.e. magnitude)
    
        e.g. Growth Rate. """

    class AspectTrigger(Enum):
        EACH_TURN = 'EACH_TURN'
        ACQUIRED = 'ACQUIRED'

    label = models.CharField(max_length=30, unique=True)
    # allows for aspects such as 'Cost' which is add for this entity
    # and a subtract for another
    effects = models.ManyToManyField('ntgame.Effect')
    # this doesn't limit correctly - validation will be required
    value = models.DecimalField(max_digits=3, decimal_places=2)
    # if null, affects owning Entity
    affects = models.ForeignKey(
        Entity, on_delete=models.SET_NULL, null=True)
    trigger = models.CharField(max_length=20, choices=(AspectTrigger))
