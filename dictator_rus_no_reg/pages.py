from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass




class NormWaitPage(WaitPage):
    pass






class S_offer(Page):

    form_model = 'group'
    form_fields = ['S_transfer', 'S_self_part']

    endowments_list_views = [60, 60, 60, 100, 100, 100]
    unit_values_for_S_list_views = [1, 1, 3, 1, 3, 1]
    unit_values_for_R_list_views = [1, 3, 1, 3, 1, 1]

    # define the max constraint (built-in otree) for field S_transfer
    def S_transfer_max(self):

        treatment_key = 'treatment_' + str(self.round_number)
        treatment_num = self.session.vars[treatment_key]

        return self.endowments_list_views[treatment_num]

    # define the error message (built-in otree) if sum of values are not equal to the pie size
    def error_message(self, values):

        treatment_key = 'treatment_' + str(self.round_number)
        treatment_num = self.session.vars[treatment_key]
        if values["S_transfer"] + values["S_self_part"] != self.endowments_list_views[treatment_num]:
            return 'Сумма токенов, которые Вы отдали Участнику 2, и токенов, которые Вы оставили себе, должна равняться изначально выданной сумме токенов'


    def vars_for_template(self):
        dict_with_endowments_and_unit_values = {}

        for i in range(6):

            treatment_key = 'treatment_' + str(i+1)
            treatment_num = self.session.vars[treatment_key]

            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = self.endowments_list_views[treatment_num]

            key = 'unit_values_for_S_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = self.unit_values_for_S_list_views[treatment_num]

            key = 'unit_values_for_R_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = self.unit_values_for_R_list_views[treatment_num]

        return dict_with_endowments_and_unit_values

    def is_displayed(self):
        return self.player.id_in_group == 1


class S_prediction(Page):

    form_model = 'group'
    form_fields = ['S_prediction']

    endowments_list_views = [60, 60, 60, 100, 100, 100]
    unit_values_for_S_list_views = [1, 1, 3, 1, 3, 1]
    unit_values_for_R_list_views = [1, 3, 1, 3, 1, 1]

    def S_prediction_max(self):

        treatment_key = 'treatment_' + str(self.round_number)
        treatment_num = self.session.vars[treatment_key]

        return self.endowments_list_views[treatment_num]

    def vars_for_template(self):
        dict_with_endowments_and_unit_values = {}

        for i in range(6):

            treatment_key = 'treatment_' + str(i+1)
            treatment_num = self.session.vars[treatment_key]

            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = self.endowments_list_views[treatment_num]

            key = 'unit_values_for_S_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = self.unit_values_for_S_list_views[treatment_num]

            key = 'unit_values_for_R_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = self.unit_values_for_R_list_views[treatment_num]

        return dict_with_endowments_and_unit_values

    def is_displayed(self):
        return self.player.id_in_group == 1








class R_prediction(Page):

    form_model = 'group'
    form_fields = ['R_prediction']

    endowments_list_views = [60, 60, 60, 100, 100, 100]
    unit_values_for_S_list_views = [1, 1, 3, 1, 3, 1]
    unit_values_for_R_list_views = [1, 3, 1, 3, 1, 1]

    def R_prediction_max(self):

        treatment_key = 'treatment_' + str(self.round_number)
        treatment_num = self.session.vars[treatment_key]

        return self.endowments_list_views[treatment_num]



    def vars_for_template(self):
        dict_with_endowments_and_unit_values = {}

        for i in range(6):

            treatment_key = 'treatment_' + str(i+1)
            treatment_num = self.session.vars[treatment_key]

            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = self.endowments_list_views[treatment_num]

            key = 'unit_values_for_S_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = self.unit_values_for_S_list_views[treatment_num]

            key = 'unit_values_for_R_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = self.unit_values_for_R_list_views[treatment_num]

        return dict_with_endowments_and_unit_values

    def is_displayed(self):
        return self.player.id_in_group == 2






class R_action(Page):

    form_model = 'group'
    form_fields = ['R_min_offer']

    endowments_list_views = [60, 60, 60, 100, 100, 100]
    unit_values_for_S_list_views = [1, 1, 3, 1, 3, 1]
    unit_values_for_R_list_views = [1, 3, 1, 3, 1, 1]

    def R_min_offer_max(self):

        treatment_key = 'treatment_' + str(self.round_number)
        treatment_num = self.session.vars[treatment_key]

        return self.endowments_list_views[treatment_num]

    def vars_for_template(self):
        dict_with_endowments_and_unit_values = {}

        for i in range(6):

            treatment_key = 'treatment_' + str(i+1)
            treatment_num = self.session.vars[treatment_key]

            key = 'endowment_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = self.endowments_list_views[treatment_num]

            key = 'unit_values_for_S_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = self.unit_values_for_S_list_views[treatment_num]

            key = 'unit_values_for_R_iter_' + str(i + 1)
            dict_with_endowments_and_unit_values[key] = self.unit_values_for_R_list_views[treatment_num]

        return dict_with_endowments_and_unit_values

    def is_displayed(self):
        return self.player.id_in_group == 2


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_round_attributes()
        self.group.set_payoffs()
        self.group.prediction_payoffs()
        self.group.set_paying_round_attributes()
        self.group.set_final_payoffs()
        self.group.set_linguistic_forms()


class S_final_results(Page):

    def is_displayed(self):
        return (self.player.id_in_group == 1 and self.round_number == 6)

class R_final_results(Page):

   def is_displayed(self):
        return (self.player.id_in_group == 2 and self.round_number == 6)




page_sequence = [
    Introduction,
    NormWaitPage,
    S_offer,
    S_prediction,
    R_prediction,
    R_action,
    ResultsWaitPage,
    S_final_results,
    R_final_results
    ]
