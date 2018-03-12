from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants


class Introduction(Page):
    pass


class NormWaitPage(WaitPage):
    pass


class S_offer(Page):

    form_model = models.Group
    form_fields = ['S_transfer', 'S_prediction_1', 'S_prediction_2', 'S_prediction_3', 'S_prediction_4', 'S_prediction_5', 'S_prediction_6', 'S_prediction_7', 'S_prediction_8']

    endowments_list_views = [100, 50, 100]
    predictions_1_list_views = [45, 15, 15]
    predictions_2_list_views = [75, 30, 30]
    predictions_3_list_views = [105, 45, 45]
    predictions_4_list_views = [150, 63, 66]
    predictions_5_list_views = [195, 87, 84]
    predictions_6_list_views = [225, 105, 105]
    predictions_7_list_views = [255, 120, 120]
    predictions_8_list_views = [285, 135, 135]

    def S_transfer_max(self):
        return self.endowments_list_views[self.subsession.round_number - 1]

    def S_prediction_1_max(self):
        return self.predictions_1_list_views[self.subsession.round_number - 1]
    def S_prediction_2_max(self):
        return self.predictions_2_list_views[self.subsession.round_number - 1]
    def S_prediction_3_max(self):
        return self.predictions_3_list_views[self.subsession.round_number - 1]
    def S_prediction_4_max(self):
        return self.predictions_4_list_views[self.subsession.round_number - 1]
    def S_prediction_5_max(self):
        return self.predictions_5_list_views[self.subsession.round_number - 1]
    def S_prediction_6_max(self):
        return self.predictions_6_list_views[self.subsession.round_number - 1]
    def S_prediction_7_max(self):
        return self.predictions_7_list_views[self.subsession.round_number - 1]
    def S_prediction_8_max(self):
        return self.predictions_8_list_views[self.subsession.round_number - 1]


    def vars_for_template(self):
        dict_with_endowments = {}
        for i in range(3):

            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments[key] = models.Constants.endowments_list[i]
            key = 'factor_iter_' + str(i + 1)
            dict_with_endowments[key] = models.Constants.factors_list[i]

        return dict_with_endowments

    def is_displayed(self):
        return self.player.id_in_group == 1

class R_prediction(Page):

    form_model = models.Group
    form_fields = ['R_prediction']

    endowments_list_views = [100, 50, 100]

    def R_prediction_max(self):
        return self.endowments_list_views[self.subsession.round_number - 1]

    def vars_for_template(self):
        dict_with_endowments = {}
        for i in range(3):
            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments[key] = models.Constants.endowments_list[i]
            key = 'factor_iter_' + str(i + 1)
            dict_with_endowments[key] = models.Constants.factors_list[i]

        return dict_with_endowments

    def is_displayed(self):
        return self.player.id_in_group == 2


class ResultsWaitPage1(WaitPage):

    def after_all_players_arrive(self):
        self.group.gen_mult_transfer()

class R_offer(Page):

    form_model = models.Group
    form_fields = ['R_transfer']

    def R_transfer_max(self):
        return self.group.mult_transfer

    def vars_for_template(self):
        dict_with_endowments = {}
        for i in range(3):
            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments[key] = models.Constants.endowments_list[i]
            key = 'factor_iter_' + str(i + 1)
            dict_with_endowments[key] = models.Constants.factors_list[i]

        return dict_with_endowments

    def is_displayed(self):
        return self.player.id_in_group == 2

class ResultsWaitPage2(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()
        self.group.set_final_payoffs()


class Results_S(Page):

    def vars_for_template(self):
        dict_with_endowments = {}
        for i in range(3):
            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments[key] = models.Constants.endowments_list[i]
            key = 'factor_iter_' + str(i + 1)
            dict_with_endowments[key] = models.Constants.factors_list[i]

        return dict_with_endowments

    def is_displayed(self):
        return self.player.id_in_group == 1

class Results_R(Page):

    def vars_for_template(self):
        dict_with_endowments = {}
        for i in range(3):
            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments[key] = models.Constants.endowments_list[i]
            key = 'factor_iter_' + str(i + 1)
            dict_with_endowments[key] = models.Constants.factors_list[i]

        return dict_with_endowments

    def is_displayed(self):
        return self.player.id_in_group == 2


class Results_Final_S(Page):

    def vars_for_template(self):
        dict_with_payment_round = {}
        key = 'payment_round'
        dict_with_payment_round[key] = self.session.vars['paying_round']
        return dict_with_payment_round

    def is_displayed(self):
        return (self.subsession.round_number == 3 and self.player.id_in_group == 1)

class Results_Final_R(Page):

    def vars_for_template(self):
        dict_with_payment_round = {}
        key = 'payment_round'
        dict_with_payment_round[key] = self.session.vars['paying_round']
        return dict_with_payment_round

    def is_displayed(self):
        return (self.subsession.round_number == 3 and self.player.id_in_group == 2)
page_sequence = [
    Introduction,
    S_offer,
    R_prediction,
    ResultsWaitPage1,
    R_offer,
    ResultsWaitPage2,
    Results_S,
    Results_R,
    Results_Final_S,
    Results_Final_R,
    NormWaitPage
]
