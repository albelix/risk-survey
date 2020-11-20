from __future__ import division

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'covid_survey'
    players_per_group = None
    num_rounds = 1

    IncrementChoices5DNK=[
        [1, 'Безусловно увеличился'],
        [2, 'Скорее увеличился'],
        [3, 'Не изменился'],
        [4, 'Скорее уменьшился'],
        [5, 'Безусловно уменьшился'],
        [6, 'Затрудняюсь ответить'],
    ]

    AgreementChoices4DNK=[
        [1, 'Совершенно согласен'],
        [2, 'Скорее согласен'],
        [3, 'Скорее не согласен'],
        [4, 'Совершенно не согласен'],
        [5, 'Затрудняюсь ответить'],
    ]

    TrustChoices4DNK=[
        [1, 'Полностью доверяю'],
        [2, 'В некоторой степени доверяю'],
        [3, 'Не очень доверяю'],
        [4, 'Совсем не доверяю'],
        [5, 'Затрудняюсь ответить'],
    ]

    SimilarChoices6DNK=[
        [1, 'Очень похож на меня'],
        [2, 'Похож на меня'],
        [3, 'Отчасти похож на меня'],
        [4, 'Немного похож на меня'],
        [5, 'Не похож на меня'],
        [6, 'Совсем не похож на меня'],
        [7, 'Затрудняюсь ответить'],
    ]

    AgreementChoices5DNK=[
        [1, 'Совершенно согласен'],
        [2, 'Скорее согласен'],
        [3, 'И да и нет'],
        [4, 'Скорее не согласен'],
        [5, 'Совершенно не согласен'],
        [6, 'Затрудняюсь ответить'],
    ]

    Sibling4=[
        [1, '0'],
        [2, '1'],
        [3, '2'],
        [4, '3'],
        [5, '4 или более'],
    ]

    Region6 = [
        [1, '0'],
        [2, '1'],
        [3, '2-3'],
        [4, '4-6'],
        [5, '7 или более'],
    ]

    education_choices = [
        [1, 'Средняя школа'],
        [2, 'Среднее профессиональное образование'],
        [3, 'Незаконченное высшее образование'],
        [4, 'Высшее образование'],
        [5, 'Два и более диплома / Ученая степень'],
    ]

    #Survey1
    Inc5DNK=IncrementChoices5DNK
    #Survey2
    Agree4DNK=AgreementChoices4DNK
    #Survey3
    Trust4DNK=TrustChoices4DNK
    #Surveys4
    Similar6DNK=SimilarChoices6DNK
    #Survey5
    Agree5DNK=AgreementChoices4DNK
    #Survery6
    Sib4=Sibling4
    #Survery7
    Reg6=Region6


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def set_payoff(self):
        """Calculate payoff, which is zero for the survey"""
        self.payoff = 0

    fdb1_instructions= models.TextField(
        verbose_name= '''Были ли Вам понятны условия эксперимента, или же что-то оставалось неясным?'''
        )

    fdb1_yourdecision= models.TextField(
        verbose_name= '''Пожалуйста, объясните Ваше решение в этом эксперименте. Почему Вы поступили именно таким образом?'''
        )

    fdb1_othersdecision= models.TextField(
        verbose_name= '''Как Вы думаете, какой процент участников этого эксперимента в Вашем городе принял решение Действовать'''
        )

    fdb1_RussiaDecision = models.TextField(
        verbose_name='''Этот эксперимент проводится в разных городах России. Как Вы думаете, какой процент участников 
        этого эксперимента в России в целом принял решение Действовать? В каких городах он будет больше, в каких меньше?'''
    )

    age = models.PositiveIntegerField(verbose_name='Ваш возраст (полных лет)',
                                        min=13, max=95,
                                        initial=None)

    gender = models.BooleanField(initial=None,
                                choices=[[0,'Мужской'],[1,'Женский']],
                                verbose_name='Ваш пол',
                                widget=widgets.RadioSelect())

    height = models.PositiveIntegerField(verbose_name='Ваш рост (в сантиметрах)',
                                        min=100, max=240,
                                        initial=None)

    marital_status = models.PositiveIntegerField(
        verbose_name='Ваш семейный статус',
        choices=[
            [1, 'Не женаты/не замужем'],
            [2, 'Женаты/замужем'],
            [3, 'В отношениях, но официально не состоите в браке'],
            [4, 'Разведены'],
            [5, 'Живете отдельно от супруга/и'],
            [6, 'Вдовец/Вдова'],
            [7, 'Затрудняюсь ответить']
        ],
        widget=widgets.RadioSelect()
    )



    field = models.PositiveIntegerField(verbose_name='Ваша специализация (выберите наиболее подходящую)',
        choices=[[1, 'Экономика, финансы, менеджмент'], [2, 'Социальные науки, психология, политология'], [3, 'Право'],  [4, 'Международные отношения'],
                 [5, 'Математика, компьютерные, точные науки'], [6, 'Гуманитарные науки'], [7, 'Медиа, журналистика, дизайн'], [8, 'Другое']],
        widget=widgets.RadioSelect())


    city = models.PositiveIntegerField(
        verbose_name='''    Сколько человек (приблизительно) проживало в том населенном пункте, где Вы жили в возрасте 16 лет.''',
        min = 1, max=30000000,
        initial = None)

    yearsinmsc = models.PositiveIntegerField(
        verbose_name='''
    Укажите, сколько лет Вы живете в Вашем городе. Впишите число, округленное до ближайшего целого числа лет.''',
        min = 0, max=95,
        initial = None)

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
    # expect= models.StringField(
    #     verbose_name= '''Как Вы думаете, совпали ли Ваши ожидания относительно поведения Ваших партнеров в этой игре с тем, какие решения они принимали на самом деле?'''
    # )
    #
    # othercit= models.StringField(
    #     verbose_name= '''Как Вы думаете, специфично ли поведение Ваших партнеров в этой игре для жителей из их города, или будь они из других городов России,
    #     в этом эксперименте они бы делали то же самое?'''
    # )
    #
    # # univ= models.StringField(
    #     verbose_name= '''Укажите ВУЗ, в котором Вы учитесь/получили Ваше наивысшее образование.'''
    # )
    #
    # study= models.StringField(
    #     verbose_name= '''Укажите  направление подготовки, на котором Вы обучались в этом ВУЗе.'''
    # )

    riskat=models.PositiveIntegerField(
        verbose_name='''Вы любите риск или боитесь риска?''',
               choices = [
                             [1, 'Очень люблю рисковать'],
                             [2, 'Скорее люблю рисковать'],
                             [3, 'Нейтрален к риску'],
                             [4, 'Скорее боюсь рисковать'],
                             [5, 'Очень боюсь рисковать'],
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
        verbose_name='''Какое высказывание наиболее точно описывает финансовое положение вашей семьи?''',
        choices=[
            [1, 'Едва сводим концы с концами, денег не хватает на выживание;'],
            [2, 'Живем от зарплаты до зарплаты, денег хватает только на неотложные нужды;'],
            [3, 'На ежедневные расходы хватает денег, но уже покупка одежды требует накоплений;'],
            [4, 'Вполне хватает денег, даже имеются некоторые накопления, но крупные покупки требуется планировать заранее;'],
            [5, 'Можем позволить себе крупные траты при первой необходимости.'],
        ],
        widget=widgets.RadioSelect()
    )

    satis=models.PositiveIntegerField(
        verbose_name='''Учитывая все обстоятельства, насколько Вы удовлетворены вашей жизнью в целом в эти дни? (от 1 «полностью не удовлетворен» до 10 «полностью удовлетворен»)''',
          choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    widget = widgets.RadioSelectHorizontal()
    )

    trust = models.PositiveIntegerField(
        verbose_name ='''Как Вы считаете, в целом большинству людей можно доверять, или же при общении с другими людьми 
        осторожность никогда не повредит? Пожалуйста, отметьте позицию на шкале, где 1 означает "Нужно быть очень осторожным с другими людьми" и 10
        означает "Большинству людей можно вполне доверять" ''',
        choices=[1,2,3,4,5,6,7,8,9,10],
        widget=widgets.RadioSelectHorizontal()
    )

    freedom = models.PositiveIntegerField(
        verbose_name='''Некоторые люди чувствуют, что они обладают полной свободой выбора и контролируют свою жизнь, в
    то время как другие люди чувствуют, что то, что они делают, не имеет реального влияния на происходящее с ними. До какой степени эти
    характеристики применимы к Вам и Вашей жизни? Пожалуйста, отметьте позицию на шкале, где 1 означает "у меня нет свободы выбора" и 10
    означает "у меня полная свобода выбора".
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


