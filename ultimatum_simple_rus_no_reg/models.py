from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Ann'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum_simple_rus_no_reg'
    players_per_group = 2
    num_rounds = 3

    instructions_template = 'ultimatum_simple_rus_no_reg/Instructions.html'

    endowments_list = [60, 100, 120]
    payoff_if_rejected = 0

class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round



class Group(BaseGroup):

    transfer = models.IntegerField(min=0)

    # S_prediction_no = models.IntegerField()
    # S_prediction_rather_no = models.IntegerField()
    # S_prediction_so_so = models.IntegerField()
    # S_prediction_rather_yes = models.IntegerField()
    # S_prediction_yes = models.IntegerField()

    S_prediction = models.IntegerField(min=0)

    R_prediction = models.IntegerField(min=0)

    R_min_acceptance = models.IntegerField(min=0)

    S_payoff_tokens = models.IntegerField()
    R_payoff_tokens = models.IntegerField()


    def set_payoffs(self):
        if self.transfer >= self.R_min_acceptance:
            self.S_payoff_tokens = Constants.endowments_list[self.round_number - 1] - self.transfer
            self.R_payoff_tokens = self.transfer
        else:
            self.S_payoff_tokens = Constants.payoff_if_rejected
            self.R_payoff_tokens = Constants.payoff_if_rejected

    S_final_payoff = models.IntegerField()
    R_final_payoff = models.IntegerField()

    def set_final_payoffs(self):
        if self.round_number < self.session.vars['paying_round']:
            self.S_final_payoff = 0
            self.R_final_payoff = 0
        else:
            self.S_final_payoff = self.in_round(self.session.vars['paying_round']).S_payoff_tokens
            self.R_final_payoff = self.in_round(self.session.vars['paying_round']).R_payoff_tokens


class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'Sender'
        else:
            return 'Receiver'