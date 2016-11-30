from django.db import models

# Custom imports
from .src import nt_rules
from .src import nt_formulas

# Create your models here.
''' This is a meta object - potentially move to ntmeta or ntcore (depending on)
scope of future app. '''
class Rule(models.Model):

    tag = models.CharField(max_length=40)
    value = models.IntegerField(default=0)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.tag


class Kingdom(models.Model):

    name = models.CharField(max_length=200)
    island = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return self.name


class Race(models.Model):

    name = models.CharField(max_length=40,unique=True)

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


class Army(models.Model):

    soldiers = models.IntegerField()
    offspec = models.IntegerField()
    defspec = models.IntegerField()
    elites = models.IntegerField()
    thieves = models.IntegerField()


    def total_off_points(self, race):
        return  (self.soldiers * 1) + \
                (self.offspec * race.offense_spec_value) + \
                (self.elites * race.elite_offense)


    def total_def_points(self, race):
        return  (self.soldiers * 1) + \
                (self.defspec * race.defense_spec_value) + \
                (self.elites * race.elite_defense)


    def __str__(self):
        return "Army: %d" % self.id


class Province(models.Model):

    name = models.CharField("Province Name", max_length=200, default="Unknown")
    ruler = models.CharField("Ruler Name", max_length=60, default="Nameless")

    ''' Citizens that can work buildings and pay taxes. Grows based on total pop
    size and can be sped up via magic. Should grow in random increments (+-10%).
    '''
    peasants = models.IntegerField(default=0)

    ''' Money, represented by gold coins (gc) is earned by taxes and spent on
    solider upkeep and drafting expenses. '''
    money = models.IntegerField(default=0)

    ''' Total land held, gained in combat or via exploration. '''
    land = models.IntegerField(default=0)

    ''' Grows based on farms and food science. Eaten hourly by all citizens.
    Peasants will die when there is a shortage, and the province will enter a
    'starving' state. Soldiers are always fed, but the pop loss will be greater
    the greater the deficit. 0 peasants means the soliders will not be paid and
    will desert. '''
    food = models.IntegerField(default=0)

    ''' Total number of magic wielding citizens. Grows based on colleges and
    decays linearly when over-popped. '''
    mages = models.IntegerField(default=0)

    ''' Currency for spells. Grows hourly based on number of towers, but Decays
    over a certain amount, once again based on total number of towers. This is
    determined by ntgame.formulas.rune_decay() '''
    runes = models.IntegerField(default=0)

    ''' Numbers of war horses stabled. Grows based on total number of stables
    and shrinks (when over-popped) linearly '''
    warhorses = models.IntegerField(default=0)

    ''' Number of prisoners captured in battle or stolen via thievery. Will
    decay until it reaches the maximum prisoner population linearly '''
    prisoners = models.IntegerField(default=0)

    ''' Difference between aid sent and received. Draws taxes based on
    relationship to networth. Decays using ntgame.formulas.tb_decay '''
    trade_balance = models.IntegerField(default=0)


    race = models.ForeignKey(Race,
        on_delete=models.CASCADE,
        null=False,
        blank=False)

    army = models.ForeignKey(Army,
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    kingdom = models.ForeignKey(Kingdom,
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    ''' Effects is a list of positive and negative effects currently held by a
    province. These are different from states that are situation based, NOT
    necessarily time based. '''
    # effects = models.ForeignKey(Effects, on_delete=models.CASCADE)

    # calculated based on number of peasants vs jobs available
    # 100 jobs available and 80 peasants is NOT 80% (need better formula)
    def building_efficiency(self):
        return 100

    ''' Networth is calculated by adding up every piece of a province and
    multiplying that piece by a set value. For example, each acre of land is
    worth 4gc so a province with 100 acres and nothing else is worth 400gc. '''
    def networth(self):
        return 0

    def __str__(self):
        return "%s of %s (%d:%d)" % \
            ( self.name,
              self.kingdom.name,
              self.kingdom.island,
              self.kingdom.number )
