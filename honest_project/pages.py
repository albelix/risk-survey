from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import json

class Intro(Page):
    pass

class Decision(Page):
    form_model = 'player'
    form_fields = ['answer']
    # def get_form_fields(self):
    #    return ['answer']


class Belief(Page):
    form_model = 'player'
    form_fields = ['forecast', 'belief']

    # def get_form_fields(self):
    #     return ['forecast']
    # def get_form_fields(self):
    #     return ['gender']
    # def get_form_fields(self):
    #     return ['age']

class Results(Page):
    pass
    # form_model = 'player'
    # form_fields=['age', 'gender']

page_sequence = [
    Intro,
    Decision,
    Belief,
    Results
]
