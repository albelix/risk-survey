from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Role)
        yield (pages.Valuation)
        if "player" == "Seller":
            yield (pages.Subrole, {"subrole": "auctioneer"})
#            yield (pages.Bids_Sellers, {'sellerbid': c(4.2)})
#            if "subrole" == "auctioneer":
            yield (pages.No_Bids_Sellers)
        elif "player" == "Buyer":
            yield (pages.Subrole, {"subrole": "participant"})
#            if "subrole" == "participant":
            yield (pages.Bids_Buyers, {'buyerchoice': 0, 'buyerbid': c(4.2)})
#                yield (pages.No_Bids_Buyers)
#        yield (pages.NormWaitPage)
#        yield (pages.ResultsWaitPage3)
        yield (pages.Results)


