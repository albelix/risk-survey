from random import Random

from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random

author = 'Alexis Belianin'

doc = """
Covid solidarity game 

"""


class Constants(BaseConstants):
    name_in_url = 'covid'
    players_per_group = None
    num_rounds = 1
    xhome = 30
    yout = 50
    costlo = 40
    costhi = 150
    priori = 0.1
    problo = 0.8
    probhi = 0.2
    R0 = 4
    Numsubj = 50

    numberhi = models.IntegerField(initial=31)
    numberlo = models.IntegerField(initial=31)



class Subsession(BaseSubsession):
    pass


class Player(BasePlayer):
    Out = models.BooleanField(initial=None,
                              choices=[[0, 'Остаюсь'], [1, 'Выхожу']],
                              verbose_name='Ваше решение',
                              widget=widgets.RadioSelect())

class Group(BaseGroup):
   def set_decisions(self):
        players = self.get_players()
        doout = [p.Out for p in players]
        self.Numout = sum(doout)
        # self.prob=self.Numout/Constants.Numobj

        #prob infected
        rng = random.Random(Constants.Numsubj)
        # numberlo = models.IntegerField(rng.randint(0,Constants.Numsubj))
        infectresh = rng.randint(0, Constants.Numsubj)
        #prob light ill
        rng = random.Random(Constants.Numsubj)
        # numberlo = models.IntegerField(rng.randint(0,Constants.Numsubj))
        numberlo = rng.randint(0, 1)
        #prob heavy ill
        rng = random.Random(Constants.Numsubj)
        # numberhi = models.IntegerField(rng.randint(0,Constants.Numsubj))
        numberhi = rng.randint(0, 1)

        #prob

        def set_payoffs(self):
            matout = (0,
                      0.014959649804959,
                      0.028926286230067,
                      0.041852746182563,
                      0.053722317942361,
                      0.087542080119919,
                      0.097422476956453,
                      0.111923725969301,
                      0.120336618841166,
                      0.151529884414938,
                      0.158257715824445,
                      0.171391950676541,
                      0.176950206122137,
                      0.181881126079613,
                      0.217971821126488,
                      0.222016243979124,
                      0.23365653936417,
                      0.236941365117563,
                      0.272147594034651,
                      0.274827824353784,
                      0.285602904512178,
                      0.287770432710175,
                      0.322260096754849,
                      0.324035602425055,
                      0.334181524981761,
                      0.335619523402103,
                      0.369593431737331,
                      0.379406716750365,
                      0.38049364690442,
                      0.390133742709511,
                      0.415083121531828,
                      0.424564683954,
                      0.4339938835183,
                      0.43468165108951,
                      0.468034616894144,
                      0.477304550645525,
                      0.477851149677481,
                      0.487045034996969,
                      0.520209296520585,
                      0.52,
                      0.52,
                      0.53,
                      0.57,
                      0.57,
                      0.58,
                      0.58,
                      0.64,
                      0.65,
                      0.65,
                      0.66,
                      0.7
                      )
            mathome = [0.14,
                       0.145040350195041,
                       0.131073713769933,
                       0.118147253817437,
                       0.106277682057639,
                       0.102457919880081,
                       0.092577523043547,
                       0.088076274030699,
                       0.079663381158834,
                       0.078470115585062,
                       0.071742284175555,
                       0.068608049323459,
                       0.063049793877863,
                       0.058118873920387,
                       0.062028178873512,
                       0.057983756020876,
                       0.05634346063583,
                       0.053058634882437,
                       0.057852405965349,
                       0.055172175646216,
                       0.054397095487822,
                       0.052229567289825,
                       0.057739903245151,
                       0.055964397574945,
                       0.055818475018239,
                       0.054380476597897,
                       0.060406568262669,
                       0.060593283249635,
                       0.05950635309558,
                       0.05986625729049,
                       0.064916878468172,
                       0.065435316046,
                       0.066006116481654,
                       0.065318348910484,
                       0.071965383105856,
                       0.072695449354475,
                       0.072148850322519,
                       0.072954965003031,
                       0.079790703479415,
                       0.081790703479415,
                       0.083790703479415,
                       0.085790703479415,
                       0.087790703479415,
                       0.089790703479415,
                       0.091790703479415,
                       0.093790703479415,
                       0.095790703479415,
                       0.097790703479415,
                       0.099790703479415,
                       0.101790703479415,
                       0.103790703479415
                       ]
            self.posthome = mathome[self.player.Numout]
            self.postout = matout[self.player.Numout]

        for p in self.get_players():
            if self.p.Out == 1:
                if self.matout[self.player.Numout,1]<infectresh:
                    infect=1
                    if self.numberlo<Constants.problo:
                        heavy=0
                    else:
                        heavy=1
                else:
                    infect=0
            p.payoff = Constants.yout - self.infect * (Constants.costlo * p.heavy + Constants.costhi * p.heavy)
