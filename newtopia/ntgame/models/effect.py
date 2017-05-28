# django modules
from django.db import models


""" The core component of province change """
class Effect(models.Model):

    name = models.CharField(max_length=40,unique=True)

    tag = models.CharField(max_length=40,unique=True)

    # others
    '''
    expires_at (ntdate)
    applies_at (ntate)
    '''
