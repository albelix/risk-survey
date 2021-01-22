from __future__ import division

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'my_survey_eng'
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
    name_in_url = 'my_survery_eng'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def set_payoff(self):
        """Calculate payoff, which is zero for the survey_prefrev"""
        self.payoff = 0

    name = models.StringField(verbose_name= '''Please indicate your name and surname''')

    Experiment1= models.StringField(
        verbose_name= '''Please describe briefly your strategy in Experiment 1: were you changing your decisions over tasks, and if so, in what way?'''
    )

    Experiment2= models.StringField(
        verbose_name= '''Please describe briefly your strategy in Experiment 2: were you changing your decisions over tasks, and if so, in what way?'''
    )

    Experiment3= models.StringField(
        verbose_name= '''Please describe briefly your strategy in Experiment 3: were you changing your decisions over tasks, and if so, in what way?'''
    )


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
    #
    #
    # study= models.StringField(
    #     verbose_name= '''Укажите  направление подготовки, на котором Вы обучались в этом ВУЗе.'''
    # )
    age = models.PositiveIntegerField(verbose_name='Your age (full years)',
                                        min=13, max=95,
                                        initial=None)

    height = models.PositiveIntegerField(verbose_name='Your height (in centimeters)',
                                        min=100, max=240,
                                        initial=None)

    weight = models.PositiveIntegerField(verbose_name='Your weight (in kilograms)',
                                         min=40, max=140,
                                         initial=None)

    yearcity16 = models.PositiveIntegerField(
        verbose_name='''How many people lived in the city where you had been living at age 16?''',
        min = 0, max=200000000,
        initial = None)

    riskat=models.PositiveIntegerField(
        verbose_name='''Do you like risk or do you prefer to avoid risk?''',
               choices = [
                             [1, 'I like risk'],
                             [2, 'I rather like risk'],
                             [3, 'I am neutral to risk'],
                             [4, 'I rather prefer to avoid'],
                             [5, 'I prefer to avoid risks'],
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
    # income = models.PositiveIntegerField(
    #     verbose_name='''Какое высказывание наиболее точно описывает финансовое положение вашей семьи?''',
    #     choices=[
    #         [1, 'Едва сводим концы с концами, денег не хватает на выживание;'],
    #         [2, 'Живем от зарплаты до зарплаты, денег хватает только на неотложные нужды;'],
    #         [3, 'На ежедневные расходы хватает денег, но уже покупка одежды требует накоплений;'],
    #         [4, 'Вполне хватает денег, даже имеются некоторые накопления, но крупные покупки требуется планировать заранее;'],
    #         [5, 'Можем позволить себе крупные траты при первой необходимости.'],
    #     ],
    #     widget=widgets.RadioSelect()
    # )

    satis=models.PositiveIntegerField(
        verbose_name='''Taking all your life circumstances into account, how much satisfied are you with your life right now? (1 means «completely dissatisfied», 10 means  «completely satisfied»)''',
          choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    widget = widgets.RadioSelectHorizontal()
    )
    #
    # trust = models.PositiveIntegerField(
    #     verbose_name ='''In general, do you think most people can be trused, or you can't be too cautious when dealing with people (1 means "Need to be cautions, 10 means "Most people can be trusted" ''',
    #     choices=[1,2,3,4,5,6,7,8,9,10],
    #     widget=widgets.RadioSelectHorizontal()
    # )

    freedom = models.PositiveIntegerField(
        verbose_name='''Some people feel they are free to choose and do control their lives, others believe they have no impact on their own lifes. Where are you on that scale?         (1 means "I have no freedom of choice", 2 means "I have no freedom to choose")''',
        choices=[1,2,3,4,5,6,7,8,9,10],
        widget=widgets.RadioSelectHorizontal()
    )
    rating = models.PositiveIntegerField(verbose_name='Your place in ICEF formal rating at the end of your last completed year',
        choices=[[1, 'Top 10%'], [2, 'First 1/3 but not top 10%'], [3, 'Above median but not first 1/3'],  [4, 'Below median but not last 1/3'],
                 [5, 'Last 1/3'], [6, 'Bottom 10% or no rating']],
        widget=widgets.RadioSelect())

    # city = models.StringField(
    #     verbose_name='''    What is the country and city/province of your residence?''',)

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


