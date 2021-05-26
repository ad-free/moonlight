from split_settings.tools import optional, include
from os import environ

ENV = environ.get('DJANGO_ENV') or 'dev'  # prod or dev

base_settings = [
    'base.py',
    optional('{}.py'.format(ENV))
]

include(*base_settings)
