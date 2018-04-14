# -*- coding: utf-8 -*-

from django.conf import settings
import ConfigParser

def languages():
    config = ConfigParser.ConfigParser()
    config.read(settings.L10N_FILE)
    return config.items('language')

def countries():
    config = ConfigParser.ConfigParser()
    config.read(settings.L10N_FILE)
    return config.items('country')
