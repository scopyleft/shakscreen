# -*- coding: utf-8 -*-

from django import template
import random

register = template.Library()

@register.simple_tag
def rand(mini=0, maxi=9999999):
    return random.randint(mini, maxi)