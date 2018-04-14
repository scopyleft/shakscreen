from config.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Meta
META['robots'] = 'noindex, nofollow'
GOOGLE_ANALYTICS_KEY = ''

# Email test
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

# Tests
INSTALLED_APPS += ('lib',)


# Debug toolbar
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar',)
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}
