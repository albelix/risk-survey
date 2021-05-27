from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = [
        'feedback0_strategy',
        'feedback1_Anger',
        'feedback2_Satisfaction',
        'feedback3_emotions',
        'satis',
        'feedback5_feedback',
        'feedback6_guess',
        'age',
        'female',
        'field',
        'height',
        'city',
        'yearsinmsc',
        'riskat',
        'riskKelly',
        # 'riskHL2',
        # 'riskHL3',
        # 'riskHL4',
        # 'riskHL5',
        # 'riskHL6',
        # 'riskHL7',
        # 'riskHL8',
        # 'riskHL9',
        # 'riskHL10',
        'trust',
        'freedom',
        'income',
        ]

    def before_next_page(self):
        self.player.set_payoff()

class Results(Page):
    pass

page_sequence = [
    MyPage, Results,
]
