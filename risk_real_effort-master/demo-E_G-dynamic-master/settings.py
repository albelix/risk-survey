from os import environ

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'cem',
        'display_name': "Certainty Equivalent Method",
        'num_demo_participants': 1,
        'app_sequence': ['cem'],
    },{
        'name': 'icl',
        'display_name': "Iterative Choice List",
        'num_demo_participants': 1,
        'app_sequence': ['icl'],
    },{
        'name': 'mpl',
        'display_name': "Multiple Price List",
        'num_demo_participants': 1,
        'app_sequence': ['mpl'],
    },{
        'name': 'scl',
        'display_name': "Single Choice List",
        'num_demo_participants': 1,
        'app_sequence': ['scl'],
    },
]


# ISO-639 code
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = []


# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """
The apps allow conducting the certainty equivalent method (CEM), the iterative choice list procedure (ICL),
the multipe price list method (MPL), and the single choice list procedure (SCL) to elicit individual level 
risk preferences in different variants and parameterizations by adapting the documented variables in config.py.
"""

# don't share this with anybody.
SECRET_KEY = 'rqufeuag=zz^=t87nfz4q7rsj)_h2dxj6$gijwt%hz@zb0)ixq'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
