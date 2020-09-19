# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Tatyana'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'bribery_effort_info_IT'
    players_per_group = 3
    endowment = c(10)
    prize = c(10)
    num_rounds = 5
# c() necessary?
    task_time = 300
    max_task_amount = 10000000

    training_answer_A_correct = c(17)
    training_answer_B_correct = c(6)
    training_answer_C_correct = c(17)

def shuffling_subgroup(matrix):
        group_matrix = [list(col) for col in zip(*matrix)]
        for column in group_matrix:
            random.shuffle(column)
        return list(zip(*group_matrix))

class Subsession(BaseSubsession):

    def get_supergroup_contributions(self, supergroup):
        players = [p for p in self.get_players() if p.participant.vars.get('supergroup') == supergroup]
        groups = list(set([p.group for p in players]))
        return [(g.contribution_A+g.contribution_B)/2 for g in groups]

    def get_average_supergroup_contrib(self, supergroup):
        if self.session.vars.get('supergroups'):
            all_contribs = self.get_supergroup_contributions(supergroup)
            return sum(all_contribs) / len(all_contribs)
        return

    def creating_session(self):
        if self.round_number == 1:
            paying_rounds = random.sample(range(1, Constants.num_rounds), 1)
            self.session.vars['paying_rounds'] = paying_rounds

        matrix = self.get_group_matrix()
        if self.session.num_participants == 24:
            self.session.vars['supergroups'] = True
            left = matrix[:4]
            right = matrix[4:]
            if self.round_number == 1:
                for g in left:
                    for p in g:
                        p.participant.vars['supergroup'] = 'left'
                for g in right:
                    for p in g:
                        p.participant.vars['supergroup'] = 'right'
            new_left = shuffling_subgroup(left)
            new_right = shuffling_subgroup(right)
            new_matrix = new_left + new_right
            self.set_group_matrix(new_matrix)


class Group(BaseGroup):
    prize = models.CharField(
    choices=['giocatore A', 'giocatore B'],
    doc="""to whom prize is allocated""",
    widget=widgets.RadioSelect())


    contribution_A = models.IntegerField(
        min=0, max=Constants.endowment,
        doc="""The amount contributed by the player""",
    )

    contribution_B = models.IntegerField(
        min=0, max=Constants.endowment,
        doc="""The amount contributed by the player""",
    )

    task_corrects_A = models.IntegerField(default=0)
    task_corrects_B = models.IntegerField(default=0)

    def set_pay(self):
        if self.prize=='giocatore A':
            for p in self.get_players():
                if p.role() == "giocatore A":
                    p.pay= (Constants.endowment  - self.contribution_A + Constants.prize)
                elif p.role() == "giocatore B":
                    p.pay= (Constants.endowment  - self.contribution_B)
                elif p.role() == "giudice":
                    p.pay= (Constants.endowment + self.contribution_A + self.contribution_B)

        else:
            for p in self.get_players():
                if p.role() == "giocatore A":
                    p.pay= (Constants.endowment  - self.contribution_A)
                elif p.role() == "giocatore B":
                    p.pay= (Constants.endowment  - self.contribution_B + Constants.prize)
                elif p.role() == "giudice":
                    p.pay= (Constants.endowment + self.contribution_A + self.contribution_B)


    def set_payoff(self): # this is the payoff of the paid rounds
        for player in self.get_players():
            for rounds in self.session.vars['paying_rounds']:
                if player.round_number == rounds:
                    player.payoff = player.pay


class Player(BasePlayer):
    def role(self):
        if self.id_in_group==1:
            return "giocatore A"
        elif self.id_in_group==2:
            return "giocatore B"
        else:
            return "giudice"

    last_correct_answer = models.IntegerField()
    tasks_correct = models.IntegerField(default=0)
    tasks_attempted = models.IntegerField(default=0)

    pay=models.CurrencyField()

    training_answer_A = models.IntegerField(verbose_name='Participant A would have')
    training_answer_B = models.IntegerField(verbose_name='Participant B would have')
    training_answer_C = models.IntegerField(verbose_name='Judge would have')







