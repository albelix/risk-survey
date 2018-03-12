from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'trust_rus_no_reg'
    players_per_group = 2
    num_rounds = 3

    instructions_template = 'trust_rus_no_reg/Instructions.html'

    endowments_list = [100, 50, 100]
    factors_list = [3, 3, 1.5]


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round


class Group(BaseGroup):


    S_transfer = models.IntegerField(min=0)

    S_prediction_1 = models.IntegerField(min=0)
    S_prediction_2 = models.IntegerField(min=0)
    S_prediction_3 = models.IntegerField(min=0)
    S_prediction_4 = models.IntegerField(min=0)
    S_prediction_5 = models.IntegerField(min=0)
    S_prediction_6 = models.IntegerField(min=0)
    S_prediction_7 = models.IntegerField(min=0)
    S_prediction_8 = models.IntegerField(min=0)

    R_prediction = models.IntegerField(min=0)

    R_transfer = models.IntegerField(min=0)

    mult_transfer = models.FloatField()
    def gen_mult_transfer(self):
        self.mult_transfer = self.S_transfer*Constants.factors_list[self.round_number - 1]

    S_payoff_tokens = models.IntegerField()
    R_payoff_tokens = models.IntegerField()

    def set_payoffs(self):
        self.S_payoff_tokens = Constants.endowments_list[self.round_number - 1] - self.S_transfer + self.R_transfer
        self.R_payoff_tokens = self.mult_transfer - self.R_transfer


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
