# django modules
from django.db import models


class Effect(models.Model):
    """ The core component of province change """

    """ e.g. Peasant Growth - would signify that applying this effect,
    with a given magnitude would impact how fast peasants grow per turn."""
    name = models.CharField(max_length=40,unique=True)

    """ Code used to identify the effect, like a key. """
    tag = models.CharField(max_length=40,unique=True)

    # others to be implemented
    '''
    expires_at (ntdate)
    applies_at (ntate)
    '''
