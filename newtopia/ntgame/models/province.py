# system modules
import inspect

# django modules
from django.db import models
from ntmeta.models import NetworthValue
from django.contrib.auth.models import User

# Custom imports
from ntgame.src import nt_rules
from ntgame.src import nt_formulas
from ntgame.src.nt_exceptions import InvalidMapException

# App imports
from .kingdom import Kingdom
from .military import Military
from .race import Race


class Province(models.Model):

    name = models.CharField("Province Name", max_length=200, null=False)
    ruler = models.CharField("Ruler Name", max_length=60, null=False)

    ''' Citizens that can work buildings and pay taxes. Grows based on total pop
    size and can be sped up via magic. Should grow in random increments (+-10%).
    '''
    peasants = models.IntegerField(default=1000)

    ''' Money, represented by gold coins (gc) is earned by taxes and spent on
    solider upkeep and drafting expenses. '''
    money = models.IntegerField(default=10000)

    ''' Total land held, gained in combat or via exploration. '''
    land = models.IntegerField(default=500)

    ''' Grows based on farms and food science. Eaten hourly by all citizens.
    Peasants will die when there is a shortage, and the province will enter a
    'starving' state. Soldiers are always fed, but the pop loss will be greater
    the greater the deficit. 0 peasants means the soliders will not be paid and
    will desert. '''
    food = models.IntegerField(default=8000)

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

    military = models.OneToOneField(Military,
        on_delete=models.CASCADE,
        primary_key=False)

    infrastructure = models.OneToOneField(Infrastructure,
        on_delete=models.CASCADE,
        primary_key=False)

    kingdom = models.ForeignKey(Kingdom,
        on_delete=models.CASCADE,
        null=False,
        blank=False)

    owner = models.ForeignKey(User,
        on_delete=models.SET_NULL,
        null=False,
        blank=False)


    ''' The networth mapping dictionary '''
    MAP = {}


    ''' Return the value of a property '''
    def get(self, key):
        k = key.lower()

        if hasattr(self,k):
            print("we have %s" % k)
            return getattr(self,k)
        else:
            print("we don't have %s" % k)
            raise InvalidMapException(key)


    ''' Land un-built '''
    @property
    def vacant_land(self):
        return self.land


    ''' Land built '''
    @property
    def built_land(self):
        return 0


    ''' Total number of science points acquired via any means '''
    @property
    def total_science_points(self):
        # self.science.total()
        return 0


    ''' Effects is a list of positive and negative effects currently held by a
    province. These are different from states that are situation based, NOT
    necessarily time based. '''
    # effects = models.ForeignKey(Effects, on_delete=models.CASCADE)

    # calculated based on number of peasants vs jobs available
    # 100 jobs available and 80 peasants is NOT 80% (need better formula)
    @property
    def building_efficiency(self):
        return 100


    ''' Networth is calculated by adding up every piece of a province and
    multiplying that piece by a set value. For example, each acre of land is
    worth 4gc so a province with 100 acres and nothing else is worth 400gc.

    Requires a valid property map.'''
    def calc_networth(self, nwmap):
        nw = 0

        try:
            for key, value in nwmap.items():
                toadd = self.get(key) * value

                # debug
                print("Adding %d to networth" % (toadd))

                nw += int(toadd)
        except InvalidMapException:
            nw = -1

        return nw

        ''' This property will set a property called nwpa (Networth Per Acre)
        which will otherwise be 0. This avoids calculating networth twice.
        This kind of makes because there's no point having a nwpa property
        without networth - and networth should always be dynamic because it
        should be the thing you notice if your province has been hit or opped. '''
        @property
        def networth(self):

            self.MAP = \
            dict((q.prop, q.value) for q in NetworthValue.objects.all())

            networth = self.calc_networth(self.MAP)

            self.nwpa = float(networth / self.land)

            return networth


        def __str__(self):
            return "%s of %s (%d:%d)" % \
                ( self.name,
                  self.kingdom.name,
                  self.kingdom.island,
                  self.kingdom.number )
