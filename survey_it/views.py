from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants, Group, Subsession, Player

class Survey(Page):
    form_model = 'player'
    form_fields = ['age',
                   'gender', 'height', 'field', 'riskat', 'income', 'satis', 'trust', 'freedom']

page_sequence = [
    Survey]

