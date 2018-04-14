import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__));

sys.path.extend([
    current_dir,
    os.path.join(current_dir, 'packages'),
])
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.prod'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
