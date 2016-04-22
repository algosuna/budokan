from .base import *

DEBUG = True

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

INSTALLED_APPS += [
    'debug_toolbar',
]

try:
    from local_settings import *
except ImportError:
    pass
