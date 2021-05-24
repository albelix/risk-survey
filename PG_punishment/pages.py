from . import models
from ._builtin import Page, WaitPage
from .models import Constants
# from django.forms.models import inlineformset_factory
# from django import forms

class Contribution(Page):
    form_model = models.Player
    form_fields = ['contribution']

    def vars_for_template(self):
        return {
            'current_round': self.subsession.round_number
        }


class BeforePunWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_pgg_payoffs()
        # self.group.set_pgg_self()


class Results0(Page):
    ...

# class PunishForm(Page):
#     class Meta:
#         model = models.Punish
#         fields=('pun')


class PunPage(Page):
    form_model = models.Player
    # form_model = 'player'
    # def get_form_fields(player):
    #     if player.id_in_group == 1:
    #         return [ 'pun_2', 'pun_3', 'pun_4', 'pun_5']
    #     elif player.id_in_group == 2:
    #         return [ 'pun_1', 'pun_3', 'pun_4', 'pun_5']
    #     elif player.id_in_group == 3:
    #         return [ 'pun_1', 'pun_2', 'pun_4', 'pun_5']
    #     elif player.id_in_group == 4:
    #         return [ 'pun_1', 'pun_2', 'pun_3', 'pun_5']
    #     else:
    #         return [ 'pun_1', 'pun_2', 'pun_3', 'pun_4']

    #form_fields = ['pun_1', 'pun_2', 'pun_3', 'pun_4', 'pun_5']

    def vars_for_template(self):
        frm = self.get_form()
        others = self.player.get_others_in_group()
        return {
            'data': zip(frm, others)
        }
        # return{
        #     'player.retained_income'
        # }

    def get_form_fields(self):
         return ['pun_{}'.format(i.id_in_group) for i in self.player.get_others_in_group()]

class ResultsWaitPage1(WaitPage):
    def after_all_players_arrive(self):
#        self.group.set_payoffs()
        for p in self.group.get_players():
            p.set_pun()
            p.set_payoff()

    # def after_all_players_arrive(self):
    #     for p in self.group.get_players():
    #         p.final_payoff()



class Results1(Page):
    pass

class Results(Page):
    # form_model = models.Player

    def vars_for_template(self):
        self.player.my_method()
        others = self.player.get_others_in_group()
        oth_payoffs = [sum([p.payoff for p in i.in_all_rounds()]) for i in others]  # final_payoff
        oth_contributions = [sum([p.contribution for p in i.in_all_rounds()]) for i in others]
 #       my_payoff = sum([p.final_payoff for p in self.player.in_all_rounds()]),
 #       my_contribution = sum([p.contribution for p in self.player.in_all_rounds()])

        return {'other_players_data': zip(others, oth_payoffs, oth_contributions),
#                'participant_payoff': my_payoff,
#                'total_contribution': my_contribution
        }


class ResultsSummary(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds
  #      return self.player.pay_round == subsession.playing_round

    def vars_for_template(self):
        return {
            'total_pgg_payoff': sum([p.pgg_payoff for p in self.player.in_all_rounds()]),
            'total_contribution': sum([p.contribution for p in self.player.in_all_rounds()]),
            'total_punishment_received': sum([p.punishment_received for p in self.player.in_all_rounds()]),
            'total_punishment_sent': sum([p.punishment_sent for p in self.player.in_all_rounds()]),
            'participant_payoff': sum([p.payoff for p in self.player.in_all_rounds()]), #+ self.retained_income  final_payoff
            'total_pay': self.player.in_round(self.session.vars['paying_round']).payoff,
            'paying_round': self.session.vars['paying_round'],
            'player_in_all_rounds': self.player.in_all_rounds(),
        }

page_sequence = [
    Contribution,
    BeforePunWP,
    Results0,
    PunPage,
    ResultsWaitPage1,
    Results1,
    Results,
    ResultsSummary
]
