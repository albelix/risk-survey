from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
One player decides how to divide a certain amount between himself and the other
player.

See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.

"""


class Constants(BaseConstants):
    name_in_url = 'dictator_rus'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'dictator_rus/Instructions.html'

    # Initial amount allocated to the dictator
    endowment = 100


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):

    kept = models.IntegerField(
        doc="""Amount dictator decided to keep for himself""",
        min=0, max=Constants.endowment,
        verbose_name='Теперь, пожалуйста, решите, сколько Вы хотите оставить себе (от 0 до %i) у.е.' % Constants.endowment
    )

    p1_region = models.CharField()
    p2_region = models.CharField()

    p1_payoff = models.IntegerField()
    p2_payoff = models.IntegerField()

    def set_payoffs(self):
        self.p1_payoff = self.kept
        self.p2_payoff = Constants.endowment - self.kept


class Player(BasePlayer):
    pass
