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
    name_in_url = 'dictator_rus_no_reg'
    players_per_group = 2
    num_rounds = 12

    instructions_template = 'dictator_rus_no_reg/Instructions.html'

    # Initial amount allocated to the dictator
    endowments_list = [75, 40, 40, 60, 60, 40, 100, 75, 50, 100, 50, 60]
    unit_values_for_S_list = [1, 1, 3, 1, 3, 1, 1, 1, 1, 3, 3, 1]
    unit_values_for_R_list = [3, 1, 1, 3, 1, 3, 1, 1, 3, 1, 1, 1]
    satisfaction_scales_list = [[8,16,24,32,40,48,56,64], [5,10,15,20,25,30,35,40], [5,10,15,20,25,30,35,40],
                                [8,16,24,32,40,48,56,60], [8,16,24,32,40,48,56,60], [5,10,15,20,25,30,35,40],
                                [15,25,35,50,65,75,85,95], [8,16,24,32,40,48,56,64], [5,10,15,20,25,30,35,40],
                                [15,25,35,50,65,75,85,95], [5,10,15,20,25,30,35,40], [8,16,24,32,40,48,56,60]]


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round


class Group(BaseGroup):

    # def round_number(self):
    #     return self.subsession.round_number

    transfer = models.IntegerField(min=0)

    prediction_S = models.IntegerField(choices=[1, 2, 3, 4, 5])

    prediction_R = models.IntegerField(min=0)

    R_sat_1 = models.IntegerField(choices=[1, 2, 3, 4, 5])
    R_sat_2 = models.IntegerField(choices=[1, 2, 3, 4, 5])
    R_sat_3 = models.IntegerField(choices=[1, 2, 3, 4, 5])
    R_sat_4 = models.IntegerField(choices=[1, 2, 3, 4, 5])
    R_sat_5 = models.IntegerField(choices=[1, 2, 3, 4, 5])
    R_sat_6 = models.IntegerField(choices=[1, 2, 3, 4, 5])
    R_sat_7 = models.IntegerField(choices=[1, 2, 3, 4, 5])
    R_sat_8 = models.IntegerField(choices=[1, 2, 3, 4, 5])

    S_payoff_tokens = models.IntegerField()
    R_payoff_tokens = models.IntegerField()
    S_payoff_ecu = models.IntegerField()
    R_payoff_ecu = models.IntegerField()

    def set_payoffs(self):
        self.S_payoff_tokens = Constants.endowments_list[self.round_number - 1] - self.transfer
        self.R_payoff_tokens = self.transfer
        self.S_payoff_ecu = self.S_payoff_tokens*Constants.unit_values_for_S_list[self.round_number - 1]
        self.R_payoff_ecu = self.R_payoff_tokens*Constants.unit_values_for_R_list[self.round_number - 1]

    S_final_payoff = models.IntegerField()
    R_final_payoff = models.IntegerField()

    def set_final_payoffs(self):
        if self.round_number < self.session.vars['paying_round']:
            self.S_final_payoff = 0
            self.R_final_payoff = 0
        else:
            # self.S_final_payoff = self.in_round(self.session.vars['paying_round']).S_payoff_tokens*Constants.unit_values_for_S_list[self.session.vars['paying_round'] - 1]
            # self.R_final_payoff = self.in_round(self.session.vars['paying_round']).R_payoff_tokens*Constants.unit_values_for_R_list[self.session.vars['paying_round'] - 1]

            self.S_final_payoff = self.in_round(self.session.vars['paying_round']).S_payoff_ecu
            self.R_final_payoff = self.in_round(self.session.vars['paying_round']).R_payoff_ecu

class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'Sender'
        else:
            return 'Receiver'
