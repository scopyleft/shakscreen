# -*- coding: utf-8 -*-

from django import template
from django.conf import settings
import ConfigParser

register = template.Library()

@register.filter
def lang(short):
    config = ConfigParser.ConfigParser()
    config.read(settings.L10N_FILE)
    return config.get('language', short)
    

@register.filter
def lang_loop(iterable):
    list = []
    for i in iterable:
        list.append(lang(i))
    return list


@register.filter
def country(short):
    config = ConfigParser.ConfigParser()
    config.read(settings.L10N_FILE)
    return config.get('country', short.upper(), "")
    

@register.filter
def country_loop(iterable):
    list = []
    for i in iterable:
        list.append(country(i))
    return list
