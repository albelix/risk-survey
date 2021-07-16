from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


# variables for all templates
# --------------------------------------------------------------------------------------------------------------------
def vars_for_all_templates(self):
    pass
#        'quit': c(Constants.quit),
#        'probability': "{0:,.0f}".format(Constants.probability) + "%"
#     return {
#         'select_return': player.income,
#         'select_volatility':  player.volatility,
#         'select_dropdown':  player.dropdown,
#     }

class Instructions(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

class Decision(Page):
    def is_displayed(self):
        form_fields = ['income', 'volatility', 'drawdown']

class Run(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass

class Results(Page):
    pass


page_sequence = [
    Instructions,
    Decision,
    Run,
    ResultsWaitPage,
    Results
]
