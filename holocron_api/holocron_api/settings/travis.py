from base import *  # noqa

DEBUG = True

SECRET_KEY = 'NOT_SO_SECRET_KEY'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'travis_ci_test',
        'USER': 'postgres',
        'HOST': 'localhost'
    }
}
