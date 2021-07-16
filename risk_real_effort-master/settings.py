from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']
EXTENSION_APPS = ['realefforttask']
SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

ROOMS = [{'display_name': 'LESH',
          'name': 'lesh'}]

SESSION_CONFIGS = [
    {
        'name': 'realefforttask',
        'display_name': "Realefforttask",
        'num_demo_participants': 1,
        'app_sequence': ['realefforttask','cem', 'mpl', 'my_survey_eng'],
    },
    {
        'name': 'cem',
        'display_name': "cem",
        'num_demo_participants': 1,
        'app_sequence': ['cem'],
    },
    {
        'name': 'icl',
        'display_name': "icl",
        'num_demo_participants': 1,
        'app_sequence': ['icl'],
    },
    {
        'name': 'mpl',
        'display_name': "mpl",
        'num_demo_participants': 1,
        'app_sequence': ['mpl'],
    },
    {
        'name': 'scl',
        'display_name': "scl",
        'num_demo_participants': 1,
        'app_sequence': ['scl','my_survey_eng'],
    },
    {
        'name': 'dynrisk',
        'display_name': "dynrisk",
        'num_demo_participants': 1,
        'app_sequence': ['dynrisk', 'my_survey_eng'],
    },
    {
        'name': 'my_survey_rus',
        'display_name': "my_survey_rus",
        'num_demo_participants': 1,
        'app_sequence': ['my_survey_rus'],
    },
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True


ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '%b&b2$lb8fz%#e0^$z=0+*)ydmjcqo6d#my4rlzck%11^od_hc'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
