"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

setting_module= 'core.deployment_settings' if 'RENDER_EXTERNAL_HOSTNAME' in os.environ else 'settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', setting_module)

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()
