# system modules
import inspect

# django modules
from django.db import models


class Military(models.Model):

    soldiers = models.IntegerField(default=0)
    offspec = models.IntegerField(default=0)
    defspec = models.IntegerField(default=0)
    elites = models.IntegerField(default=0)
    thieves = models.IntegerField(default=0)

    @property


    def total_off_points(self, race):
        # base offense
        raw_offense = (self.soldiers * 1) + \
            (self.offspec * self.province.race.offense_spec_value) + \
            (self.elites * self.province.race.elite_offense)


        return  (self.soldiers * 1) + \
                (self.offspec * self.province.race.offense_spec_value) + \
                (self.elites * self.province.race.elite_offense) + \
                (self.province.war_horses )


    def total_def_points(self, race):
        return  (self.soldiers * 1) + \
                (self.defspec * race.defense_spec_value) + \
                (self.elites * race.elite_defense)


    def __str__(self):
        if hasattr(self,"province"):
            return "Military of %s" % self.province.name
        else:
            return "Unassigned Military"
