#-*- coding:utf-8 -*-

from django.conf import settings
from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    sender = forms.EmailField(max_length=100, required=True)
    subject = forms.CharField(max_length=100,  required=True)
    body = forms.CharField(widget=forms.widgets.Textarea, required=True)
    
    def send(self):
        recipient = settings.CONTACT_EMAIL
        if not isinstance(recipient, list) or not isinstance(recipient, tuple):
            recipient = (recipient,)
        send_mail(\
            self.cleaned_data['subject'],\
            self.cleaned_data['body'],\
            self.cleaned_data['sender'],\
            recipient\
        )