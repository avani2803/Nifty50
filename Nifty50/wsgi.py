"""
WSGI config for Nifty50 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import threading
import time
from django.core.wsgi import get_wsgi_application
from Nifty50Web.util.WebClient import initThread

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nifty50.settings')

application = get_wsgi_application()


threading.Thread(target=initThread).start()