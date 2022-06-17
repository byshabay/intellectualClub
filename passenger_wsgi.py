# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/s/shabba0u/shabba0u.beget.tech/intellectualClub')
sys.path.insert(1, '/home/s/shabba0u/.local/lib/python3.8/site-packages>')
os.environ['DJANGO_SETTINGS_MODULE'] = 'intellectual.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()