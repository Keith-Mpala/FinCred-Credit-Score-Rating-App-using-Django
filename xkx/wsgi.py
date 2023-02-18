"""
WSGI config for xkx project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xkx.settings')

application = get_wsgi_application()

#web: gunicorn xkx.wsgi:application --error-logfile /var/log/gunicorn-error.log --access-logfile /var/log/gunicorn-access.log

