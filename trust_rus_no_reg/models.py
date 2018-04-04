from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from random import shuffle
import math



class Constants(BaseConstants):
    name_in_url = 'T'
    players_per_group = 2
    num_rounds = 3

    instructions_template = 'trust_rus_no_reg/Instructions.html'

    endowments_list = [100, 50, 100]
    factors_list = [3, 3, 1.5]
    ecu_to_rur = 2

    predictions_offer_r1 = [10,20,30,40,50,60,70,80,90,100]
    predictions_return_r1 = [30,60,90,120,150,180,210,240,270,300]

    predictions_offer_r2 = [5,10,15,20,25,30,35,40,45,50]
    predictions_return_r2 = [15,30,45,60,75,90,105,120,135,150]

    predictions_offer_r3 = [10,20,30,40,50,60,70,80,90,100]
    predictions_return_r3 = [15,30,45,60,75,90,105,120,135,150]


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:

            #define payment round
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round



class Group(BaseGroup):

    # S answers

    S_transfer = models.IntegerField(min=0)

    S_prediction_1 = models.IntegerField(min=0)
    S_prediction_2 = models.IntegerField(min=0)
    S_prediction_3 = models.IntegerField(min=0)
    S_prediction_4 = models.IntegerField(min=0)
    S_prediction_5 = models.IntegerField(min=0)
    S_prediction_6 = models.IntegerField(min=0)
    S_prediction_7 = models.IntegerField(min=0)
    S_prediction_8 = models.IntegerField(min=0)
    S_prediction_9 = models.IntegerField(min=0)
    S_prediction_10 = models.IntegerField(min=0)

    # R answers
    R_prediction = models.IntegerField(min=0)

    R_transfer = models.IntegerField(min=0)


    # set S transfer * factor (note the rounding rules!!)

    mult_transfer = models.IntegerField()

    def gen_mult_transfer(self):
        self.mult_transfer = math.ceil(self.S_transfer * Constants.factors_list[self.round_number - 1])


    # set current payoffs (players don't observe these)

    S_payoff = models.IntegerField()
    R_payoff = models.IntegerField()

    def set_payoffs(self):
        self.S_payoff = Constants.endowments_list[self.round_number - 1] - self.S_transfer + self.R_transfer
        self.R_payoff = self.mult_transfer - self.R_transfer


    S_prediction = models.IntegerField(min=0)
    S_prediction_payoff = models.FloatField()
    R_prediction_payoff = models.FloatField()

    def prediction_payoffs(self):


        # closeness for S predictions about how much R will return
        closest_offer_counter = 0
        min_distance = 100000000

        if self.round_number == 1:
            for i in range(10):
                if (self.S_transfer - Constants.predictions_offer_r1[i])**2 < min_distance:
                    min_distance = (self.S_transfer - Constants.predictions_offer_r1[i])**2
                    closest_offer_counter = i
        if self.round_number == 2:
            for i in range(10):
                if (self.S_transfer - Constants.predictions_offer_r2[i])**2 < min_distance:
                    min_distance = (self.S_transfer - Constants.predictions_offer_r1[i])**2
                    closest_offer_counter = i
        if self.round_number == 3:
            for i in range(10):
                if (self.S_transfer - Constants.predictions_offer_r3[i])**2 < min_distance:
                    min_distance = (self.S_transfer - Constants.predictions_offer_r1[i])**2
                    closest_offer_counter = i


        list_with_S_predictions = [self.S_prediction_1,self.S_prediction_2,self.S_prediction_3, self.S_prediction_4,
                                  self.S_prediction_5,self.S_prediction_6,self.S_prediction_7,self.S_prediction_8,
                                   self.S_prediction_9, self.S_prediction_10]

        self.S_prediction = list_with_S_predictions[closest_offer_counter]


        self.S_prediction_payoff = round((Constants.endowments_list[self.round_number - 1]/2) * (1 - abs((self.S_prediction - self.R_transfer)/self.mult_transfer)), 2)

        # closeness for R predictions about how much S will transfer
        self.R_prediction_payoff = round((Constants.endowments_list[self.round_number - 1]/2) * (1 - abs((self.R_prediction - self.S_transfer)/Constants.endowments_list[self.round_number - 1])), 2)



    # set paying round attributes

    paying_round_num = models.IntegerField()
    pie_size_final = models.IntegerField()
    factor_final = models.FloatField()

    mult_transfer_final = models.FloatField()
    S_prediction_final = models.IntegerField()
    R_transfer_final = models.IntegerField()
    R_prediction_final = models.IntegerField()
    S_transfer_final = models.IntegerField()


    def set_paying_round_attributes(self):

        self.paying_round_num = self.session.vars['paying_round']

        self.pie_size_final = Constants.endowments_list[self.paying_round_num - 1]
        self.factor_final = round(Constants.factors_list[self.paying_round_num - 1],1)

        if self.round_number < self.paying_round_num:
            self.mult_transfer_final = 0
            self.S_prediction_final = 0
            self.R_transfer_final = 0
            self.R_prediction_final = 0
            self.S_transfer_final = 0
        elif self.round_number >= self.paying_round_num:
            self.mult_transfer_final = self.in_round(self.paying_round_num).mult_transfer
            self.S_prediction_final = self.in_round(self.paying_round_num).S_prediction
            self.R_transfer_final = self.in_round(self.paying_round_num).R_transfer
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