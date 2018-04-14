#-*- coding:utf-8 -*-

from django.views.generic import TemplateView
from app.models import SimplePage
from django.http import Http404
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from filmography.models import PlayReference

def simplepage(request, slug=None):
    if slug:
        try:
            page = SimplePage.objects.filter(slug=slug)[0]
        except IndexError:
            raise Http404('No page with slug "%s" was found.' % slug)
    else:
        try:
            page = SimplePage.objects.filter(reference='homepage')[0]
        except IndexError:
            raise Http404('Homepage is a SimplePage with reference set to "homepage". No such page was found.')
    
    return render_to_response('simplepage.html', RequestContext(request, locals()))
