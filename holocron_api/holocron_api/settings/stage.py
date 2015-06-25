from base import *  # noqa
import os

DEBUG = False

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('HOLOCRON_DB_NAME'),
        'USER': get_env_variable('HOLOCRON_DB_USER'),
        'PASSWORD': get_env_variable('HOLOCRON_DB_PASS'),
        'HOST': get_env_variable('HOLOCRON_DB_HOST'),
        'PORT': get_env_variable('HOLOCRON_DB_PORT')
    }
}
