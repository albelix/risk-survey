from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Mydecisions(Page):
    form_model = 'player'
    form_fields = [
                   'name',
                   'Experiment1',
                   'Experiment2',
                   'Experiment3'
                   ]


# class City(Page):
#     form_model = 'player'
#     form_fields = ['city',
#                    'yearsinmsc', 'mscyourcity', 'achieve', 'deput']


class Yourself(Page):
    form_model = 'player'
    form_fields = ['age',
                    'height',
                    'weight',
                    'yearcity16',
                    'riskat',
                    'satis',
                    'freedom',
                    'rating']

# class polit(Page):
#     form_model = 'player'
#     form_fields = ['freedom',
#                        'politics',
#                        'leftright',
#                        'owner',
#                        'responsibility',
#                        'democracy',
#                         'democracy_today',
#                         'renovation',
#                         'attitudes']

    def before_next_page(self):
        self.player.set_payoff()


page_sequence = [
    Mydecisions, Yourself #, polit, City,
]
