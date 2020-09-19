from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'AB'

doc = """
Clarke-Groves implementation problem
"""


class Constants(BaseConstants):
    name_in_url = 'CGimplem'
    players_per_group = 5
    num_rounds = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def role(self):
        if self.id_in_group != 1:
            return 'principal'
        if self.id_in_group == 1:
            return 'agent'

