"""
WSGI config for transtext project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

reload(sys)     
sys.setdefaultencoding("utf-8")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "transtext.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)