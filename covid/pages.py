from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Welcome(Page):
    pass

class Instruction_main(Page):
    pass

class Instruction_table(Page):
    form_model = 'player'
    form_fields = ['Out']

class Decision(Page):
    pass

class Waiting(Page):
    pass

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Welcome, Instruction_main, Instruction_table, Waiting, ResultsWaitPage, Results]
