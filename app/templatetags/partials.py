#-*- coding:utf-8 -*-

from django import template
from django.conf import settings
from django.http import HttpResponseRedirect
from app.forms import ContactForm

register = template.Library()

@register.inclusion_tag('partials/googlemaps.html')
def googlemaps():
    pass

@register.inclusion_tag('partials/contact_form.html', takes_context=True)
def contact_form(context):
    form = ContactForm()
    request = context['request']
    message = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send()
            message = "Votre demande a bien été envoyée"
            form = ContactForm() # empty form
    return {'form': form, 'message': message}
