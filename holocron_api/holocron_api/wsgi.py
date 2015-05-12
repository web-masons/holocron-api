"""
WSGI config for holocron_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the app's directory to the PYTHONPATH
sys.path.append('/vagrant/holocron_api')
sys.path.append('/vagrant/holocron_api/holocron-api')
sys.path.append('/vagrant/holocron_api/api')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "holocron_api.settings")

application = get_wsgi_application()
