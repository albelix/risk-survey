from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class NormWaitPage(WaitPage):
    pass

class S_offer(Page):

    form_model = 'group'
    form_fields = ['transfer', 'prediction_S']

    endowments_list_views = [75, 40, 40, 60, 60, 40, 100, 75, 50, 100, 50, 60]

    def transfer_max(self):
        return self.endowments_list_views[self.subsession.round_number - 1]

    def vars_for_template(self):
        dict_with_endowments_and_unit_values = {}
        for i in range(12):

            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = models.Constants.endowments_list[i]
            key = 'unit_values_for_S_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = models.Constants.unit_values_for_S_list[i]
            key = 'unit_values_for_R_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = models.Constants.unit_values_for_R_list[i]

        return dict_with_endowments_and_unit_values

    def is_displayed(self):
        return self.player.id_in_group == 1

class R_prediction(Page):

    form_model = 'group'
    form_fields = ['prediction_R', 'R_sat_1', 'R_sat_2', 'R_sat_3', 'R_sat_4', 'R_sat_5', 'R_sat_6', 'R_sat_7', 'R_sat_8']

    endowments_list_views = [75, 40, 40, 60, 60, 40, 100, 75, 50, 100, 50, 60]

    def transfer_max(self):
        return self.endowments_list_views[self.subsession.round_number - 1]

    def vars_for_template(self):
        dict_with_endowments_and_unit_values = {}
        for i in range(12):

            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = models.Constants.endowments_list[i]
            key = 'unit_values_for_S_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = models.Constants.unit_values_for_S_list[i]
            key = 'unit_values_for_R_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = models.Constants.unit_values_for_R_list[i]

        return dict_with_endowments_and_unit_values

    def is_displayed(self):
        return self.player.id_in_group == 2



class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()
        self.group.set_final_payoffs()


class Results_S(Page):

    def vars_for_template(self):
        dict_with_endowments_and_unit_values = {}
        for i in range(12):

            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = models.Constants.endowments_list[i]
            key = 'unit_values_for_S_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = models.Constants.unit_values_for_S_list[i]
            key = 'unit_values_for_R_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = models.Constants.unit_values_for_R_list[i]

        return dict_with_endowments_and_unit_values

    def is_displayed(self):
        return self.player.id_in_group == 1

class Results_R(Page):

    def vars_for_template(self):
        dict_with_endowments_and_unit_values = {}
        for i in range(12):

            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = models.Constants.endowments_list[i]
            key = 'unit_values_for_S_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = models.Constants.unit_values_for_S_list[i]
            key = 'unit_values_for_R_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = models.Constants.unit_values_for_R_list[i]

        return dict_with_endowments_and_unit_values
    def is_displayed(self):
        return self.player.id_in_group == 2


class Results_Final_S(Page):

    def vars_for_template(self):
        dict_with_payment_round = {}
        key = 'payment_round'
        dict_with_payment_round[key] = self.session.vars['paying_round']
        return dict_with_payment_round

    def is_displayed(self):
        return (self.subsession.round_number == 12 and self.player.id_in_group == 1)

class Results_Final_R(Page):

    def vars_for_template(self):
        dict_with_payment_round = {}
        key = 'payment_round'
        dict_with_payment_round[key] = self.session.vars['paying_round']
        return dict_with_payment_round

    def is_displayed(self):
        return (self.subsession.round_number == 12 and self.player.id_in_group == 2)

page_sequence = [
    Introduction,
    S_offer,
    R_prediction,
    ResultsWaitPage,
    Results_S,
    Results_R,
    Results_Final_S,
    Results_Final_R,
    NormWaitPage
    ]
