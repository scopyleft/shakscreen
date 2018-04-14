from django.conf import settings
from django.template import add_to_builtins

# Autoload templatetags set in settings
for source in settings.TEMPLATE_TAGS:
    add_to_builtins(source)