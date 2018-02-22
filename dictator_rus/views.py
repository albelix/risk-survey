from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass

class region_question_p1(Page):
    form_model = models.Group
    form_fields = ['p1_region']

    def is_displayed(self):
        return self.player.id_in_group == 1


class region_question_p2(Page):
    form_model = models.Group
    form_fields = ['p2_region']

    def is_displayed(self):
        return self.player.id_in_group == 2

class CommonWaitPage(WaitPage):
    pass

class Offer_p1(Page):
    form_model = models.Group
    form_fields = ['kept']

    def is_displayed(self):
        return self.player.id_in_group == 1

class p2(Page):

    def is_displayed(self):
        return self.player.id_in_group == 2

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

    def vars_for_template(self):
        if self.player.id_in_group == 2:
            body_text = "Подождите, пока Участник 1 примет свое решение"
        else:
            body_text = 'Пожалуйста, подождите.'
        return {'body_text': body_text}


class Results(Page):
    def offer(self):
        return Constants.endowment - self.group.kept

    def vars_for_template(self):
        return {
            'offer': Constants.endowment - self.group.kept,
        }


page_sequence = [
    Introduction,
    region_question_p1,
    region_question_p2,
    CommonWaitPage,
    Offer_p1,
    p2,
    ResultsWaitPage,
    Results
]
