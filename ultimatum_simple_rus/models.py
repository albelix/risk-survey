from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Ann'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum_simple_rus'
    players_per_group = 2
    num_rounds = 1

    endowment = 100
    payoff_if_rejected = 0

class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):

    sent_amount = models.IntegerField(min = 0, max = 100)
    acceptance = models.BooleanField(choices=[[True, 'Да'], [False, 'Нет']])

    p1_region = models.CharField()
    p2_region = models.CharField()

    p1_payoff = models.IntegerField()
    p2_payoff = models.IntegerField()


    def set_payoffs(self):
        if self.acceptance:
            self.p1_payoff = Constants.endowment - self.sent_amount
            self.p2_payoff = self.sent_amount
        else:
            self.p1_payoff = Constants.payoff_if_rejected
            self.p2_payoff = Constants.payoff_if_rejected

class Player(BasePlayer):
    pass
