"""Settings for testing zinnia on SQLite"""
from holocron_api.holocron_api.settings import *

SECRET_KEY = 'TRAVIS_NOT_SO_SECRET_KEY'

DATABASES = {
    'default': {
       'NAME': 'holocron-api.db',
       'ENGINE': 'django.db.backends.sqlite3'
    }
}