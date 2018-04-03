from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants



class Intro(Page):
    pass

class NormWaitPage(WaitPage):
    pass



class S_offer(Page):

    form_model = 'group'
    form_fields = ['S_transfer', 'S_self_part']

    endowments_list_views = [60, 100, 120]

    def S_transfer_max(self):
        return self.endowments_list_views[self.subsession.round_number - 1]

    def error_message(self, values):
        if values["S_transfer"] + values["S_self_part"] != self.endowments_list_views[self.subsession.round_number - 1]:
            return 'Сумма экю, которые Вы отдали Участнику 2, и экю, которые Вы оставили себе, должна равняться изначально выданной сумме экю'


    def vars_for_template(self):
        dict_with_endowments = {}
        for i in range(3):

            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments[key] = models.Constants.endowments_list[i]

        return dict_with_endowments

    def is_displayed(self):
        return self.player.id_in_group == 1


class S_prediction(Page):

    form_model = 'group'
    form_fields = ['S_prediction']

    endowments_list_views = [60, 100, 120]


    def S_prediction_max(self):
        return self.endowments_list_views[self.subsession.round_number - 1]

    def vars_for_template(self):
        dict_with_endowments = {}
        for i in range(3):

            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments[key] = models.Constants.endowments_list[i]

        return dict_with_endowments

    def is_displayed(self):
        return self.player.id_in_group == 1






class R_answer(Page):

    form_model = 'group'
    form_fields = ['R_min_acceptance']

    endowments_list_views = [60, 100, 120]

    def R_min_acceptance_max(self):
        return self.endowments_list_views[self.subsession.round_number - 1]

    def vars_for_template(self):
        dict_with_endowments = {}
        for i in range(3):

            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments[key] = models.Constants.endowments_list[i]

        return dict_with_endowments

    def is_displayed(self):
        return self.player.id_in_group == 2


class R_prediction(Page):

    form_model = 'group'
    form_fields = ['R_prediction']

    endowments_list_views = [60, 100, 120]

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
        self.group.prediction_payoffs()
        self.group.set_paying_round_attributes()
        self.group.set_final_payoffs()



class S_final_results(Page):

    def is_displayed(self):
        return (self.player.id_in_group == 1 and self.round_number == 3)

class R_final_results(Page):

   def is_displayed(self):
        return (self.player.id_in_group == 2 and self.round_number == 3)




page_sequence = [
    Intro,
    NormWaitPage,
    S_offer,
    S_prediction,
    R_answer,
    R_prediction,
    ResultsWaitPage,
    S_final_results,
    R_final_results,
    NormWaitPage
    ]