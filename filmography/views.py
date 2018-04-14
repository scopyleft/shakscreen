#-*- coding:utf-8 -*-

from filmography.models import Contributor, Film, Play, Analysis, PlayReference
from django.http import Http404
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def contributor(request, slug):
    try:
        contributor = Contributor.objects.filter(slug=slug)[0]
    except IndexError:
        return Http404("No contributor matches slug \"%s\"", slug)
    return render_to_response('contributor.html', RequestContext(request, locals()))

def film(request, slug):
    try:
        film = Film.objects.get(slug=slug) # get_object_or_404
        actors = ()
        for character in film.filmcharacter_set.all():
            actors += (character.fullname,)
    except IndexError:
        return Http404("No film matches slug \"%s\"", slug)
    return render_to_response('film.html', RequestContext(request, locals()))

def play_films(request, slug):
    play = Play.objects.filter(slug=slug)[0]
    return render_to_response('play_films.html', RequestContext(request, locals()))

def analysis(request, slug):
    try:
        analysis = Analysis.objects.filter(slug=slug)[0]
    except IndexError:
        return Http404("No analysis matches slug \"%s\"", slug)
    return render_to_response('analysis.html', RequestContext(request, locals()))

def film_description(request, id):
    reference = PlayReference.objects.get(pk=id)
    if not reference:
        raise Http404('No reference with id %d was found' % id)
    return render_to_response('film_description.html', RequestContext(request, locals()))

def film_quotation(request, id):
    reference = PlayReference.objects.get(pk=id)
    if not reference:
        raise Http404('No reference with id %d was found' % id)
    return render_to_response('film_quotation.html', RequestContext(request, locals()))