from base import *  #noqa

DEBUG = True

SECRET_KEY = 'NOT_SO_SECRET_KEY'

DATABASES = {
    'default': {
        'ENGINE': django.db.backends.postgresql_psycopg2,
        'NAME': 'holocron',
        'USER': 'django-test',
        'PASSWORD': 'testing'
        'HOST': 'localhost'
    }
}

