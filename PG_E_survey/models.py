from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Alexis Belianin'

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'PG_E_survey'
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

    feedback0_strategy= models.TextField(
        verbose_name= '''Опишите в общих чертах Вашу стратегию в игре: как Вы выбирали сколько внести в групповой проект, 
        изменяли ли свою стратегию со временем и почему и т.д.'''
        )

    feedback1_Anger= models.TextField(
        verbose_name= '''Испытывали ли Вы возмущение поведением других игроков в игре, и если да, то кого, когда и почему?'''
        )

    feedback2_Satisfaction = models.TextField(
        verbose_name='''Испытывали ли Вы чувство удовлетворения от поведения других игроков в игре, и если да, то кого, когда и почему?'''
        )

    feedback3_emotions = models.TextField(
        verbose_name='''Влияли ли как-то эти эмоции на Ваше поведение в игре? А другие эмоции (какие?)'''
        )

    satis=models.PositiveIntegerField(
        verbose_name='''Оцените в целом Ваше настроение сегодня по шкале от 1 «ужасное» до 10 «превосходное»)''',
          choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    widget = widgets.RadioSelectHorizontal()
    )

    feedback5_feedback = models.TextField(
        verbose_name='''Повлияло ли как-то на Ваше настроение то, что Вы испытали в ходе этой игры, и если да, то каким образом?'''
        )

    feedback6_guess = models.TextField(
        verbose_name='''Как Вы думаете, верно ли Вы угадывали эмоции других участников этой игры?'''
        )

    age = models.PositiveIntegerField(verbose_name='Ваш возраст (полных лет)',
                                        min=13, max=95,
                                        initial=None)

    female = models.BooleanField(initial=None,
                                choices=[[0,'Мужской'],[1,'Женский']],
                                verbose_name='Ваш пол',
                                widget=widgets.RadioSelect())

    height = models.PositiveIntegerField(verbose_name='Ваш рост (в сантиметрах)',
                                        min=100, max=240,
                                        initial=None)

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
    Укажите, сколько лет Вы живете в Москве. Впишите число, округленное до ближайшего целого числа лет.''',
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

    riskKelly=models.PositiveIntegerField(
        verbose_name='''Вы выиграли в лотерею 1 млн. рублей. Хороший знакомый предлагает Вам вложить некоторую часть из этой суммы
        в предприятие, которое удвоит вложенную Вами сумму с вероятностью 1/3, или окажется неудачным и Вы потеряете все вложенные деньги с 
        вероятностью 2/3. Какую сумму Вы готовы вложить в это предприятие?''',
               choices = [
                             [1, '1 млн.рублей'],
                             [2, '800 тысяч рублей'],
                             [3, '600 тысяч рублей'],
                             [4, '400 тысяч рублей'],
                             [5, '200 тысяч рублей'],
                             [6, 'Нисколько, все оставлю у себя'],
                         ],
                         widget = widgets.RadioSelect()
    )


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

