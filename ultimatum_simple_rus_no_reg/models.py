from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
from random import shuffle

author = 'Ann'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'U'
    players_per_group = 2
    num_rounds = 3


    instructions_template = 'ultimatum_simple_rus_no_reg/Instructions.html'

    endowments_list = [60, 100, 120]
    ecu_to_rur = 2

    payoff_if_rejected = 0

class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:

            #define payment round
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round



class Group(BaseGroup):

    # S answers

    S_transfer = models.IntegerField(min=0)
    S_self_part = models.IntegerField(min=0)

    S_prediction = models.IntegerField(min=0)


    # R answers

    R_min_acceptance = models.IntegerField(min=0)

    R_prediction = models.IntegerField(min=0)


    # set current payoffs (players don't observe these)

    S_payoff = models.IntegerField()
    R_payoff = models.IntegerField()

    def set_payoffs(self):
        if self.S_transfer >= self.R_min_acceptance:
            self.S_payoff = Constants.endowments_list[self.round_number - 1] - self.S_transfer
            self.R_payoff = self.S_transfer
        else:
            self.S_payoff = Constants.payoff_if_rejected
            self.R_payoff = Constants.payoff_if_rejected

    S_prediction_payoff = models.FloatField()
    R_prediction_payoff = models.FloatField()

    def prediction_payoffs(self):
        self.S_prediction_payoff = round((Constants.endowments_list[self.round_number - 1]/2) * (1 - abs((self.S_prediction - self.R_min_acceptance)/Constants.endowments_list[self.round_number - 1])),2)
        self.R_prediction_payoff = round((Constants.endowments_list[self.round_number - 1]/2) * (1 - abs((self.R_prediction - self.S_transfer)/Constants.endowments_list[self.round_number - 1])),2)


    # set paying round attributes

    paying_round_num = models.IntegerField()
    pie_size_final = models.IntegerField()

    S_prediction_final = models.IntegerField()
    R_min_acceptance_final = models.IntegerField()
    R_prediction_final = models.IntegerField()
    S_transfer_final = models.IntegerField()

    def set_paying_round_attributes(self):

        self.paying_round_num = self.session.vars['paying_round']

        self.pie_size_final = Constants.endowments_list[self.paying_round_num-1]

        if self.round_number < self.paying_round_num:
            self.S_prediction_final = 0
            self.R_min_acceptance_final = 0
            self.R_prediction_final = 0
            self.S_transfer_final = 0
        elif self.round_number >= self.paying_round_num:
            self.S_prediction_final = self.in_round(self.paying_round_num).S_prediction
            self.R_min_acceptance_final = self.in_round(self.paying_round_num).R_min_acceptance
            self.R_prediction_final = self.in_round(self.paying_round_num).R_prediction
            self.S_transfer_final = self.in_round(self.paying_round_num).S_transfer



    # set final payoffs

    S_final_payoff = models.IntegerField()
    R_final_payoff = models.IntegerField()
    S_final_prediction_payoff = models.FloatField()
    R_final_prediction_payoff = models.FloatField()

    def set_final_payoffs(self):
        if self.round_number < self.paying_round_num:
            self.S_final_payoff = 0
            self.R_final_payoff = 0
            self.S_final_prediction_payoff = 0
            self.R_final_prediction_payoff = 0
        else:
            self.S_final_payoff = self.in_round(self.paying_round_num).S_payoff
            self.R_final_payoff = self.in_round(self.paying_round_num).R_payoff
            self.S_final_prediction_payoff = self.in_round(self.paying_round_num).S_prediction_payoff
            self.R_final_prediction_payoff = self.in_round(self.paying_round_num).R_prediction_payoff




class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'Sender'
        else:
            return 'Receiver'