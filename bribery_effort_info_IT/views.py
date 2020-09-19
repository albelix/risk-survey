# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Welcome(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1

class Introduction(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1

class Question(Page):

    form_model = models.Player
    form_fields = ['training_answer_A', 'training_answer_B', 'training_answer_C']

    def is_displayed(self):
        return self.subsession.round_number == 1

    def training_answer_C_error_message(self, value):
        if value != Constants.training_answer_C_correct:
            return 'La tua risposta "{}" gettoni riguardo il partecipante C non era coretta.'.format(value)

    def training_answer_A_error_message(self, value):
        if value != Constants.training_answer_A_correct:
            return 'La tua risposta "{}" gettoni riguardo il partecipante A non era coretta.'.format(value)

    def training_answer_B_error_message(self, value):
        if value != Constants.training_answer_B_correct:
            return 'La tua risposta "{}" gettoni riguardo il partecipante B non era coretta.'.format(value)

class Feedback(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1

class StartA(Page):
    def is_displayed(self):
        return (
            self.player.role() == "giocatore A"
        )

class StartB(Page):
    def is_displayed(self):
        return (
                self.player.role() == "giocatore B"
        )

class StartC(Page):
    def is_displayed(self):
        return (
                self.player.role() == "giudice"
        )
    timeout_seconds = 300

class ContributeA(Page):
    def is_displayed(self):
        return (
            self.player.role() == "giocatore A"
        )
    form_model = models.Group
    form_fields = ['contribution_A']


class ContributeB(Page):
    def is_displayed(self):
        return (
            self.player.role() == "giocatore B"
        )
    form_model = models.Group
    form_fields = ['contribution_B']

class Prize(Page):
    def is_displayed(self):
        return self.player.role() == "giudice"

    form_model = models.Group
    form_fields = ['prize']

class WaitTask(WaitPage):
    def after_all_players_arrive(self):
        pass

class WaitContribute(WaitPage):
    def after_all_players_arrive(self):

        for g in self.subsession.get_groups():
            for p in g.get_players():
                if g.get_player_by_id(p.id_in_group).role() =="giocatore A" :
                    g.task_corrects_A = g.get_player_by_id(p.id_in_group).tasks_correct
                elif g.get_player_by_id(p.id_in_group).role() == "giocatore B" :
                    g.task_corrects_B = g.get_player_by_id(p.id_in_group).tasks_correct


class WaitPrize(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_pay()
        self.group.set_payoff()

class Start(Page):
    def is_displayed(self):
        return (
            self.player.role() == "giocatore A" or self.player.role() == "giocatore B"
        )

class WorkTryOut(Page):
    def is_displayed(self):
        return (
            self.player.role() == "giocatore A" or self.player.role() == "giocatore B"
        )
    timer_text = "Tempo rimanente per completare questa parte:"
    timeout_seconds = 300

class ResultsJudge(Page):
    def is_displayed(self):
        return (
            self.player.role() == "giudice"
        )

class ResultsPlayerA(Page):
    def is_displayed(self):
        return (
            self.player.role() == "giocatore A"
        )

class ResultsPlayerB(Page):
    def is_displayed(self):
        return (
            self.player.role() == "giocatore B"
        )

class AllGroupsWaitPage(WaitPage):
    wait_for_all_groups = True

class Infopage (Page):

    def vars_for_template(self):
        own_supergroup = self.participant.vars['supergroup']
        return {
            'contribs': self.subsession.get_average_supergroup_contrib(own_supergroup)
        }

class Payoffs(Page):

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        round = self.session.vars['paying_rounds']
        return {"paying_round": str(round)[1:-1],
                "final_payoff": self.participant.payoff_plus_participation_fee(),
                'player_in_all_rounds': self.player.in_all_rounds()}

page_sequence = [
Welcome,
Introduction,
Question,
Feedback,
StartA,
StartB,
Start,
WaitTask,
StartC,
WorkTryOut,
ContributeA,
ContributeB,
WaitContribute,
Prize,
WaitPrize,
ResultsJudge,
ResultsPlayerA,
ResultsPlayerB,
AllGroupsWaitPage,
Infopage,
Payoffs,
]














