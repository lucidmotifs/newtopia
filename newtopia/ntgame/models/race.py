# system modules
import inspect

# django modules
from django.db import models

# Custom imports
from ntgame.src import nt_rules
from ntgame.src import nt_formulas


class Race(models.Model):

    name = models.CharField(max_length=40,unique=True)

    ''' Offensive spec name. '''
    offense_spec_name = models.CharField(max_length=40,default="Off. Spec")

    ''' Defensive spec name. '''
    defensive_spec_name = models.CharField(max_length=40,default="Def. Spec")

    ''' Elite name '''
    elite_name = models.CharField(max_length=40,default="Elite")

    ''' Offensive spec value. Default is set by over-all game rules '''
    # Could potentially use delta here instead, so new race models could be
    # built from rules instead of hardcoded value changes.
    offense_spec_value = models.IntegerField(default=nt_rules.off_spec_base())

    ''' Defensive spec value. Default is set by over-all game rules '''
    defense_spec_value = models.IntegerField(default=nt_rules.def_spec_base())

    ''' Elite values always vary from race to race '''
    elite_offense = models.IntegerField(default=0)
    elite_defense = models.IntegerField(default=0)

    ''' Each 'race rule' should be listed here... such as building effectiveness
    and if a BE == 0 then it means this cannot be built (e.g) no war horses on
    one race. '''


    def __str__(self):
        return self.name
