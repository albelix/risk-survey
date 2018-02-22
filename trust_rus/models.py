from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
This is a standard 2-player trust game where the amount sent by player 1 gets
tripled. The trust game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'trust_rus'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'trust_rus/Instructions.html'

    # Initial amount allocated to each player
    endowment = 100
    multiplication_factor = 3


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    sent_amount = models.IntegerField(
        min=0, max=Constants.endowment,
        doc="""Amount sent by P1""",
    )

    sent_back_amount = models.IntegerField(
        doc="""Amount sent back by P2""",
        min=0,
    )

    p1_region = models.CharField()
    p2_region = models.CharField()

    p1_payoff = models.IntegerField()
    p2_payoff = models.IntegerField()
    def set_payoffs(self):
        self.p1_payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
        self.p2_payoff = self.sent_amount * Constants.multiplication_factor - self.sent_back_amount


class Player(BasePlayer):

    def role(self):
        return {1: 'A', 2: 'B'}[self.id_in_group]
