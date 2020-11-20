from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import json
from django.urls import reverse

author = 'Alexis Belianin'

doc = """
Honesty and cheating project
"""


class Constants(BaseConstants):
    name_in_url = 'honest_project'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass
    #    endowment = models.IntegerField()
    #
    #    def creating_session(self):
    #        self.endowmentaa=random.randint(0,100)
    #
    # def creating_session(self):    ## this either takes endomwent from the session app in settings.py or from constants
    #     self.endowment=self.session.config.get('endowment',
    #                                            Constants.endowment)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # report_answer = models.BooleanField(choices=[[0,'Yes'],[1,'No']])
    answer = models.IntegerField(min=0, max=6, initial=None)
    # tail=models.IntegerField(min=0, max=6)

    forecast = models.IntegerField(min=0, max=6, initial=None)  # add straight away to make sure bmi is recorded in your data
    belief=models.IntegerField(min=0, max=100)
    #№gender = models.BooleanField(initial=None,
    #                            choices=[[0,'Мужской'],[1,'Женский']],
    #                            widget=widgets.RadioSelect())
    #age = models.IntegerField(min=12, max=70)
