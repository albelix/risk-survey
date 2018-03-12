from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):
    def play_round(self):
        yield (views.Introduction)

        if self.player.id_in_group == 1:
            yield (views.Offer, {"kept": 99})
            assert self.player.payoff == 99
        else:
            assert self.player.payoff == 1
        yield (views.Results)
