from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class invest(Page):
    form_model = 'player'
    form_fields = ['norm1_iis',
                   'norm2_horiz',
                   'norm3_goals',
                   'norm3a_goals',
                   'norm4_withdraw',
                   'norm5_shareinv',
                   'norm6_invstrat',
                   'norm6a_invstrat',
                   'norm7_know',
                   'norm8_risk',
                   'norm9_debt',
                   'norm10_exper',
                   'norm10a_exper',
                   'norm11_invlott',
                   'norm11down_invlott',
                   'norm11up_invlott',
                   'riskat',
                   'management',
                   ]


class MyPage(Page):
    form_model = 'player'
    form_fields = [
        'age',
        'gender',
        'field',
        'field_other',
        'family',
        'famember',
        'income',
        'budget',
        'budget_other',
        'decision',
        'satis',
        'expect',
        'trust',
        'freedom',
        ]

    def before_next_page(self):
        self.player.set_payoff()


page_sequence = [
    invest, MyPage, #, Yourself #, polit, City,
]
