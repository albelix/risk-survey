from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants



class Intro(Page):
    pass

class NormWaitPage(WaitPage):
    pass



class S_offer(Page):

    form_model = models.Group
    form_fields = ['transfer', 'S_prediction']

    endowments_list_views = [60, 100, 120]

    def transfer_max(self):
        return self.endowments_list_views[self.subsession.round_number - 1]

    def S_prediction_max(self):
        return self.endowments_list_views[self.subsession.round_number - 1]

    # form_model = models.Group
    # form_fields = ['transfer', 'S_prediction_no', 'S_prediction_rather_no', 'S_prediction_so_so', 'S_prediction_rather_yes','S_prediction_yes']

    def vars_for_template(self):
        dict_with_endowments = {}
        for i in range(3):

            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments[key] = models.Constants.endowments_list[i]

        return dict_with_endowments

    def is_displayed(self):
        return self.player.id_in_group == 1

class R_prediction(Page):

    form_model = models.Group
    form_fields = ['R_prediction', 'R_min_acceptance']

    endowments_list_views = [60, 100, 120]

    def R_min_acceptance_max(self):
        return self.endowments_list_views[self.subsession.round_number - 1]

    def R_prediction_max(self):
        return self.endowments_list_views[self.subsession.round_number - 1]


    def vars_for_template(self):
        dict_with_endowments = {}
        for i in range(3):

            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments[key] = models.Constants.endowments_list[i]

        return dict_with_endowments

    def is_displayed(self):
        return self.player.id_in_group == 2



class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()
        self.group.set_final_payoffs()


class Results_S(Page):

    def vars_for_template(self):
        dict_with_endowments = {}
        for i in range(3):

            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments[key] = models.Constants.endowments_list[i]

        return dict_with_endowments

    def is_displayed(self):
        return self.player.id_in_group == 1

class Results_R(Page):

    def vars_for_template(self):
        dict_with_endowments = {}
        for i in range(3):

            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments[key] = models.Constants.endowments_list[i]

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
    Intro,
    S_offer,
    R_prediction,
    ResultsWaitPage,
    Results_S,
    Results_R,
    Results_Final_S,
    Results_Final_R,
    NormWaitPage
    ]