from __future__ import division

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'survey_it'
# from otree.api import (
#     models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
#     Currency as c, currency_range
# )
# import random

import random

from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json


class Constants(BaseConstants):
    name_in_url = 'survey_it'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def set_payoff(self):
        """Calculate payoff, which is zero for the survey"""
        self.payoff = 0

    age = models.PositiveIntegerField(verbose_name='Tua età',
                                        min=13, max=95,
                                        initial=None)

    gender = models.BooleanField(initial=None,
                                choices=[[0,'maschio'],[1,'femmina']],
                                verbose_name='Sesso',
                                widget=widgets.RadioSelect())

    height = models.PositiveIntegerField(verbose_name='Tua altezza (in centimetri)',
                                        min=100, max=240,
                                        initial=None)


    field = models.PositiveIntegerField(verbose_name='Campo di studi',
        choices=[[1, 'Economia, finanza, gestione'], [2, 'Scienze sociali, psicologia, scienze politiche'], [3, 'Legge'],  [4, 'Relazioni internazionali'],
                 [5, 'Matematica, informatica'], [6, 'Scienze umane'], [7, 'Media, giornalismo, design'], [8, 'affari e amministrazione'], [8, 'Altro']],
        widget=widgets.RadioSelect())


    # mscyourcity = models.PositiveIntegerField(
    #     verbose_name='''
    # Можете ли вы сказать, что Москва – это ваш город?''',
    #     choices=[
    #         [1, 'Совершенно не соглас(ен)/(на)'],
    #         [2, 'Скорее не соглас(ен)/(на)'],
    #         [3, 'И не соглас(ен)/(на) и соглас(ен)/(на)'],
    #         [4, 'Скорее соглас(ен)/(на)'],
    #         [5, 'Совершенно соглас(ен)/(на)'],
    #     ],
    #     widget=widgets.RadioSelect()
    # )

    # achieve= models.StringField(
    #     verbose_name= '''Какие значимые достижения/решения московских властей последних 3 лет Вы можете
    # назвать? Напишите не более 5.'''
    # )
    #
    # deput= models.StringField(
    #     verbose_name= '''Знаете ли Вы по именам кого-нибудь из муниципальных депутатов Москвы или Московской городской
    # думы? Напишите не более 5 имен.'''
    # )
    #
    # univ= models.StringField(
    #     verbose_name= '''Укажите ВУЗ, в котором Вы учитесь/получили Ваше наивысшее образование.'''
    # )
    #
    # study= models.StringField(
    #     verbose_name= '''Укажите  направление подготовки, на котором Вы обучались в этом ВУЗе.'''
    # )

    riskat=models.PositiveIntegerField(
        verbose_name='''Ti piace il rischio o eviti il rischio ?''',
               choices = [
                             [1, 'mi piace il rischio'],
                             [2, 'mi piace abbastanza il rischio'],
                             [3, 'sono indifferente al rischio'],
                             [4, 'preferisco evitare il rischio'],
                             [5, 'evito il rischio'],
                         ],
                         widget = widgets.RadioSelect()
    )
    #
    # riskHL1=models.BooleanField(
    #     verbose_name='''Выберите одну из двух лотерей
    #     A: [1200 рублей, 0.10; 40 рублей, 0.90] или Б: [650 рублей, 0.10; 500 рублей, 0.90]''',
    #     choices = [
    #         [0, 'А'],
    #         [1, 'Б'],
    #     ],
    #     widget = widgets.RadioSelectHorizontal()
    # )
    #
    # riskHL2=models.BooleanField(
    #     verbose_name='''Выберите одну из двух лотерей
    #     A: [1200 рублей, 0.20; 40 рублей, 0.80] или Б: [650 рублей, 0.20; 500 рублей, 0.80]''',
    #     choices = [
    #         [0, 'А'],
    #         [1, 'Б'],
    #     ],
    #     widget = widgets.RadioSelectHorizontal()
    # )
    # riskHL3=models.BooleanField(
    #     verbose_name='''Выберите одну из двух лотерей
    #     A: [1200 рублей, 0.30; 40 рублей, 0.70] или Б: [650 рублей, 0.30; 500 рублей, 0.70]''',
    #     choices = [
    #         [0, 'А'],
    #         [1, 'Б'],
    #     ],
    #     widget = widgets.RadioSelectHorizontal()
    # )
    # riskHL4=models.BooleanField(
    #     verbose_name='''Выберите одну из двух лотерей
    #     A: [1200 рублей, 0.40; 40 рублей, 0.60] или Б: [650 рублей, 0.40; 500 рублей, 0.60]''',
    #     choices = [
    #         [0, 'А'],
    #         [1, 'Б'],
    #     ],
    #     widget = widgets.RadioSelectHorizontal()
    # )
    # riskHL5=models.BooleanField(
    #     verbose_name='''Выберите одну из двух лотерей
    #     A: [1200 рублей, 0.50; 40 рублей, 0.50] или Б: [650 рублей, 0.50; 500 рублей, 0.50]''',
    #     choices = [
    #         [0, 'А'],
    #         [1, 'Б'],
    #     ],
    #     widget = widgets.RadioSelectHorizontal()
    # )
    # riskHL6=models.BooleanField(
    #     verbose_name='''Выберите одну из двух лотерей
    #     A: [1200 рублей, 0.60; 40 рублей, 0.40] или Б: [650 рублей, 0.60; 500 рублей, 0.40]''',
    #     choices = [
    #         [0, 'А'],
    #         [1, 'Б'],
    #     ],
    #     widget = widgets.RadioSelectHorizontal()
    # )
    # riskHL7=models.BooleanField(
    #     verbose_name='''Выберите одну из двух лотерей
    #     A: [1200 рублей, 0.70; 40 рублей, 0.30] или Б: [650 рублей, 0.70; 500 рублей, 0.30]''',
    #     choices = [
    #         [0, 'А'],
    #         [1, 'Б'],
    #     ],
    #     widget = widgets.RadioSelectHorizontal()
    # )
    # riskHL8=models.BooleanField(
    #     verbose_name='''Выберите одну из двух лотерей
    #     A: [1200 рублей, 0.80; 40 рублей, 0.20] или Б: [650 рублей, 0.80; 500 рублей, 0.20]''',
    #     choices = [
    #         [0, 'А'],
    #         [1, 'Б'],
    #     ],
    #     widget = widgets.RadioSelectHorizontal()
    # )
    # riskHL9=models.BooleanField(
    #     verbose_name='''Выберите одну из двух лотерей
    #     A: [1200 рублей, 0.90; 40 рублей, 0.10] или Б: [650 рублей, 0.90; 500 рублей, 0.10]''',
    #     choices = [
    #         [0, 'А'],
    #         [1, 'Б'],
    #     ],
    #     widget = widgets.RadioSelectHorizontal()
    # )
    # riskHL10=models.BooleanField(
    #     verbose_name='''Выберите одну из двух лотерей
    #     A: [1200 рублей, 1.00; 40 рублей, 0.00] или Б: [650 рублей, 1.00; 500 рублей, 0.00]''',
    #     choices = [
    #         [0, 'А'],
    #         [1, 'Б'],
    #     ],
    #     widget = widgets.RadioSelectHorizontal()
    # )
    #
    income = models.PositiveIntegerField(
        verbose_name='''Quale affermazione descrive con precisione la situazione finanziaria della tua famiglia?''',
        choices=[
            [1, 'I soldi non sono sufficienti per sopravvivere;'],
            [2, 'I soldi sono sufficienti solo per i bisogni urgenti;'],
            [3, 'I soldi sono sufficienti per le spese quotidiane, ma già comprare vestiti richiede risparmi;'],
            [4, 'I soldi sono sufficienti, c’è anche qualche risparmio, ma i grandi acquisti devono essere pianificati in anticipo;'],
            [5, 'Possiamo permetterci grandi spese alla prima necessità.'],
        ],
        widget=widgets.RadioSelect()
    )

    satis=models.PositiveIntegerField(
        verbose_name='''Date tutte le circostanze, quanto sei soddisfatto della tua vita in generale? (da 1 "completamente insoddisfatto" a 10 "completamente soddisfatto")''',
          choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    widget = widgets.RadioSelectHorizontal()
    )

    trust = models.PositiveIntegerField(
        verbose_name ='''Secondo la tua opinione, in generale, la maggior parte delle persone è affidabile, o quando si comunica con le altre persone la cautela non fa mai male? Contrassegna la posizione sulla scala, dove 1 significa "Devi stare molto attento con le altre persone" e 10 significa "La maggior parte delle persone può essere completamente affidabile" ''',
        choices=[1,2,3,4,5,6,7,8,9,10],
        widget=widgets.RadioSelectHorizontal()
    )

    freedom = models.PositiveIntegerField(
        verbose_name='''Alcune persone sentono di avere completa libertà di scelta e di controllare la propria vita, mentre altre persone 
        sentono che ciò che stanno facendo non ha un impatto reale su ciò che sta loro accadendo. In che misura queste caratteristiche 
        sono applicabili a te e alla tua vita? Contrassegna la posizione sulla scala, dove 1 significa "Non ho libertà di scelta" 
        e 10 significa "Ho una totale libertà di scelta"".
    ''',
        choices=[1,2,3,4,5,6,7,8,9,10],
        widget=widgets.RadioSelectHorizontal()
    )
    #
    #
    # politics=models.PositiveIntegerField(
    #     verbose_name='''До какой степени Вы интересуетесь политикой? (от 1 «Вообще не интересуюсь» до 10 «Очень интересуюсь»)''',
    # choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    #           widget = widgets.RadioSelectHorizontal()
    # )
    #
    # leftright = models.PositiveIntegerField(
    #     verbose_name='''В политике говорят о людях "левых" (сторонники равенства и социальной справедливости) и "правых"
    #     (сторонники либерализма и конкуренции) взглядов. Как бы Вы охарактеризовали свои взгляды на шкале от 1 «крайне левые» до
    #     10 «крайне правые»?''',
    #     choices=[1,2,3,4,5,6,7,8,9,10],
    #     widget=widgets.RadioSelectHorizontal()
    # )
    #
    # owner=models.PositiveIntegerField(
    #     verbose_name='''До какой степени Вы согласны с утверждением: «Право собственности непоколебимо»?''',
    #             choices = [
    #                           [1, 'Совершенно не соглас(ен)/(на)'],
    #                           [2, 'Скорее не соглас(ен)/(на)'],
    #                           [3, 'И не соглас(ен)/(на) и соглас(ен)/(на)'],
    #                           [4, 'Скорее соглас(ен)/(на)'],
    #                           [5, 'Совершенно соглас(ен)/(-на)'],
    #                       ],
    #                       widget = widgets.RadioSelect()
    # )
    #
    # ownership=models.PositiveIntegerField(
    #     verbose_name='''Как Вы относитесь к утверждению  «Доля государственной собственности в экономике нашей страны должна быть увеличена»?
    #     Отметьте на шкале, где 1 означает, что Вы полностью не согласны с утверждением, 10 - что полностью согласны''',
    #        choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    #                  widget = widgets.RadioSelectHorizontal()
    # )
    #
    # responsibility = models.PositiveIntegerField(
    #     verbose_name='''Как Вы относитесь к утверждению  ««Правительство должно нести ответственность за благосостояние людей»?
    #     Отметьте на шкале, где 1 означает, что Вы полностью не согласны с этим утверждением, 10 - что полностью согласны''',
    #        choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    #                  widget = widgets.RadioSelectHorizontal()
    # )
    #
    # democracy = models.PositiveIntegerField(
    #     verbose_name=''' Насколько важно для Вас жить в стране, которая управляется по принципам демократии, т.е. в соответствии с волей народа?
    #     Отметьте на шкале, где 1 означает «не важно», 10 «очень важно» ''',
    #     choices=[1,2,3,4,5,6,7,8,9,10],
    #     widget=widgets.RadioSelectHorizontal()
    # )
    #
    # democracy_today=models.PositiveIntegerField(
    #     verbose_name='''Можете ли Вы сказать, что политическая система в нашей стране на сегодняшний день является демократической?
    #     Отметьте на шкале, где 1 означает «совсем не демократическая» до 10 «полностью демократическая»''',
    #         choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    #                   widget = widgets.RadioSelectHorizontal()
    # )
    # renovation = models.PositiveIntegerField(choices=[[0,'Нет, не знаю'],[1,'Что-то слышал, но не в деталях'],[2,'Да, знаю']],
    #                              verbose_name='Знаете ли вы о программе реновации ("снос пятиэтажек"), предложенной правительством Москвы?',
    #                              widget=widgets.RadioSelect()
    # )
    #
    # attitudes = models.PositiveIntegerField(verbose_name='Как вы относитесь к программе реновации, предложенной правительством Москвы?',
    #                                choices = [
    #                                    [1, 'Совершенно не одобряю'],
    #                                    [2, 'Скорее не одобряю'],
    #                                    [3, 'В чем-то не одобряю, а в чем-то одобряю'],
    #                                    [4, 'Скорее одобряю'],
    #                                    [5, 'Совершенно одобряю'],
    #                                    [6, 'Затрудняюсь ответить/ничего не знаю о ней']
    #                                ],
    #                                widget = widgets.RadioSelect()
    # )


