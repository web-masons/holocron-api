"""
WSGI config for holocron_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

from django.core.handlers.wsgi import WSGIHandler
import django
import os
import sys

# Add the app's directory to the PYTHONPATH
base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(base_path)
sys.path.append(base_path + '/holocron-api')
sys.path.append(base_path + '/holocron_api/api')


# using technique from http://bit.ly/1MQc3ae to expose vars to app
# these vars are initially set via /etc/apache2/envvars via aws user-data


class WSGIEnvironment(WSGIHandler):

    def __call__(self, environ, start_response):

        env_variables_to_pass = ['DJANGO_SETTINGS_MODULE',
                         'DJANGO_SECRET_KEY',
                         'HOLOCRON_ENV',
                         'HOLOCRON_DB_USER',
                         'HOLOCRON_DB_PASS',
                         'HOLOCRON_DB_HOST',
                         'HOLOCRON_DB_PORT',
                         'HOLOCRON_DB_NAME']

        # pass the WSGI environment variables on through to os.environ
        for var in env_variables_to_pass:
            os.environ[var] = environ.get(var, '')
        os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                              "holocron_api.settings.local")
        django.setup()
        return super(WSGIEnvironment,self).__call__(environ,start_response)

application = WSGIEnvironment()