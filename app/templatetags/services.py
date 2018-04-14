from django import template
from django.template.loader import render_to_string
from django.conf import settings

register = template.Library()

@register.simple_tag
def analytics():
    if settings.GOOGLE_ANALYTICS_KEY == '':
        return ''
    return render_to_string('services/analytics.html', {'key': settings.GOOGLE_ANALYTICS_KEY})