from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Alexis Belianin'

doc = """
Dynamic risk preferences (Reiffeisen) elicitation app
"""


class Constants(BaseConstants):
    name_in_url = 'dynrisk'
    players_per_group = None
    num_rounds = 10
    endowment = 100
    my_constant = 25
    lb = 50
    ub = 100
    don_choices = [10, 20]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    income = models.FloatField(min=3, max=25)
    volatility = models.FloatField(min=1, max=50)
    drawdown = models.FloatField(min=2, max=4)
    # bmi = models.FloatField()  # add straight away to make sure bmi is recorded in your data
    # donation = models.CurrencyField(choices=[10, 20])
    # endowment = models.CurrencyField()
    # choice_order = models.StringField()

    def get_risk(self):
        return round((self.income -2 ) * 2, 2)
