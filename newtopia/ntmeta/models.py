from django.db import models

from ntgame.models import Race, Province

# Create your models here.
''' This is a meta object - potentially move to ntmeta or ntcore (depending on)
scope of future app. '''
class Rule(models.Model):

    tag = models.CharField(max_length=40)
    value = models.IntegerField(default=0)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.tag


class NetworthValue(models.Model):

    prop = models.CharField(max_length=40)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.prop
