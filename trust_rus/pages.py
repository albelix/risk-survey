from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants


class Introduction(Page):
    pass

class region_question_p1(Page):
    form_model = 'group'
    form_fields = ['p1_region']

    def is_displayed(self):
        return self.player.id_in_group == 1


class region_question_p2(Page):
    form_model = 'group'
    form_fields = ['p2_region']

    def is_displayed(self):
        return self.player.id_in_group == 2


class NormWaitPage(WaitPage):
    pass

class Send(Page):
    """This page is only for P1
    P1 sends amount (all, some, or none) to P2
    This amount is tripled by experimenter,
    i.e if sent amount by P1 is 5, amount received by P2 is 15"""

    form_model = 'group'
    form_fields = ['sent_amount']

    def is_displayed(self):
        return self.player.id_in_group == 1


class SendBackWaitPage(WaitPage):
    pass


class SendBack(Page):
    """This page is only for P2
    P2 sends back some amount (of the tripled amount received) to P1"""

    form_model = 'group'
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        tripled_amount = self.group.sent_amount * Constants.multiplication_factor

        return {
                'tripled_amount': tripled_amount,
                'prompt':
                    'Выберете сумму, которую Вы хотите вернуть Участнику 1 (от 0 до %s):' % tripled_amount}

    def sent_back_amount_max(self):
        return self.group.sent_amount * Constants.multiplication_factor


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    """This page displays the earnings of each player"""

    def vars_for_template(self):
        return {
            'tripled_amount': self.group.sent_amount * Constants.multiplication_factor
        }


page_sequence = [
    Introduction,
    region_question_p1,
    region_question_p2,
    NormWaitPage,
    Send,
    SendBackWaitPage,
    SendBack,
    ResultsWaitPage,
    Results,
]
