#!/usr/bin/env python
import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__));

sys.path.extend([
    os.path.join(current_dir, 'packages'),
])

from django.core.management import execute_manager
import imp
try:
    import config.local # Assumed to be in the config directory.
except ImportError:
    sys.stderr.write("Error: Can't find the file 'config/local.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

import config.local

if __name__ == "__main__":
    execute_manager(config.local)
