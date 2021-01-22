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
    group_name = models.BooleanField(verbose_name='''Вы относитесь к числу
         государственных служащих или предпринимателей''',
         choices = [
             [0, 'государственный служащий'],
             [1, 'предприниматель'],
         ],
        widget = widgets.RadioSelectHorizontal()
                                )
    gender = models.BooleanField(verbose_name='''Ваш пол''',
                                choices=[
                                    [0, 'мужской'],
                                    [1, 'женский'],
                                ],
                                widget=widgets.RadioSelectHorizontal()
                                )
    age = models.IntegerField(verbose_name='''Ваш возраст''',min=20, max=70, initial=None)
    # educat = models.PositiveIntegerField(
    #     verbose_name='''Ваше образование (по специальности, выберите наиболее близкий вариант)''',
    #     choices=[
    #         [1, 'математика, программирование, инженерое дело'],
    #         [2, 'естественные науки'],
    #         [3, 'медицина'],
    #         [4, 'гуманитарные и социальные науки'],
    #         [5, 'экономика и менеджмент'],
    #         [6, 'право'],
    #         [7, 'искусство'],
    #         [8, 'военное дело'],
    #         [9, 'другое'],
    #     ],
    #     widget=widgets.RadioSelect()
    # )

    forecast_bus = models.IntegerField(min=0, max=6, initial=None)
    belief_bus = models.IntegerField(min=0, max=100, initial=None)

    forecast_gos = models.IntegerField(min=0, max=6, initial=None)
    belief_gos = models.IntegerField(min=0, max=100, initial=None)
    #№gender = models.BooleanField(initial=None,
    #                            choices=[[0,'Мужской'],[1,'Женский']],
    #                            widget=widgets.RadioSelect())
    #age = models.IntegerField(min=12, max=70)
