from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
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

class Offer_p1(Page):
    form_model = 'group'
    form_fields = ['sent_amount']

    def is_displayed(self):
        return self.player.id_in_group == 1

class p2(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2


class Acceptance_page(Page):
    form_model = 'group'
    form_fields = ['acceptance']

    def is_displayed(self):
        return self.player.id_in_group == 2

class ResultWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


page_sequence = [
    Instructions,
    region_question_p1,
    region_question_p2,
    NormWaitPage,
    Offer_p1,
    p2,
    NormWaitPage,
    Acceptance_page,
    ResultWaitPage,
    Results
]
