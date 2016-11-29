from django.db import models

# Custom imports
from .src import race
from .src import formulas

# Create your models here.
class Kingdom(models.Model):

    name = models.CharField(max_length=200)
    island = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return self.name


class Army(models.Model):

    race = models.CharField(max_length=40)
    soldiers = models.IntegerField()
    offspec = models.IntegerField()
    defspec = models.IntegerField()
    elites = models.IntegerField()
    thieves = models.IntegerField()


    def __init__(self, race="Human"):
        self.race = race


    def get_elite_off_val(self):
        return ntgame.race.get_elite_offense(self.race)


    def get_elite_def_val(self):
        return ntgame.race.get_elite_defense(self.race)


    def off_points(self):
        return  (self.soliders * 1) + \
                (self.offspec * 4) + \
                (self.elites * self.get_elite_off_val())


    def def_points(self):
        return  (self.soliders * 1) + \
                (self.defspec * 4) + \
                (self.elites * self.get_elite_def_val())


    def __str__(self):
        return "%d Soldier, %d Off Spec, %d Def Spec, %d Elites, %d Thieves"


class Province(models.Model):

    name = models.CharField("Province Name", max_length=200, default="Unknown")
    race = models.CharField("Province Race", max_length=40, default="Human")
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

    army = models.ForeignKey(Army, on_delete=models.CASCADE, null=True)
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE, null=True)

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
        return self.name
