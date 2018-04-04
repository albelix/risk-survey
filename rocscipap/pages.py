from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):

    form_model = 'player'
    form_fields = ['hum_move']
    timeout_seconds = 100

    def before_next_page(self):
        self.player.randome_move_solver()
        self.player.comp_move_solver()
        self.player.result_solver()
        self.player.result_text_solver()
        self.player.comp_move_text_solver()
        self.player.cum_result_solver()
        self.player.set_cum_payoff()
        self.player.set_cum_payoff_comp()


class Results(Page):

    form_model = 'player'

    def vars_for_template(self):
        return {'a': self.round_number,
                'cumulative_hum_payoff': sum([p.cum_payoff_hum for p in self.player.in_all_rounds()])}


page_sequence = [
    MyPage,
    Results
]
