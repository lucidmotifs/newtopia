from django.db import models

# Create your models here.
class Kingdom(models.Model):

    name = models.CharField(max_length=200)
    island = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return self.name


class Province(models.Model):

    name = models.CharField("Province Name", max_length=200)
    race = models.CharField("Province Race", max_length=40)
    ruler = models.CharField("Ruler Name", max_length=60)
    peasants = models.IntegerField()
    money = models.IntegerField()
    land = models.IntegerField()
    food = models.IntegerField()
    mages = models.IntegerField()
    runes = models.IntegerField()
    warhorses = models.IntegerField()
    prisoners = models.IntegerField()
    trade_balance = models.IntegerField()
    army = models.ForeignKey(Army, on_delete=models.CASCADE)
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)

    # calculated based on number of peasants vs jobs available
    # 100 jobs available and 80 peasants is NOT 80% (need better formula)
    def building_efficiency(self):
        return 100


    def networth(self):


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
        return Game.get_elite_offense_value(self.race)


    def get_elite_def_val(self):
        return Game.get_elite_defense_value(self.race)


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
