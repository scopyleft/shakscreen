from django.conf import settings as conf_settings

def settings(self):
    return {'settings': conf_settings}