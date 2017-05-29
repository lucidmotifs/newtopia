# system modules
import inspect

# django modules
from django.db import models

class Kingdom(models.Model):

    name = models.CharField(max_length=200)
    island = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return "%s (%d:%d)" % ( self.name, self.island, self.number )
