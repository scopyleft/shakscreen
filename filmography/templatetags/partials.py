from django import template
from filmography.models import Contributor, Film, Play
from filmography.forms import FilmSearchForm
from lib.utils import i10n

register = template.Library()

@register.inclusion_tag('partials/contributors.html')
def contributors():
    contributors = Contributor.objects.all()
    return locals()

#@register.inclusion_tag('partials/films.html')
#def films(type=None):
#    if type in ('adaptations', 'references'):
#        return getattr(Film.play_references, type)()
#    elif type is None:
#        return Film.play_references.all()
#    else:
#        raise ArgumentError('The "films" templatetag accepts optional argument that can be "adaptations" or "references. "%s" given' % type)
@register.inclusion_tag('partials/films.html')
def films(type=None): 
    if type in ('adaptations', 'references'):
        films = getattr(Film.play_references, type)()
    elif not type:
        films = Film.objects.all()
    else:
        raise ArgumentError('The "films" templatetag accepts optional argument that can be "adaptations" or "references. "%s" given' % type)
    return locals()




@register.inclusion_tag('partials/play_references.html')
def play_references():
    plays = Play.objects.all()
    return locals()

@register.inclusion_tag('partials/play_adaptations.html')
def play_adaptations():
    plays = Play.objects.all()
    return locals()

@register.inclusion_tag('partials/plays.html')
def plays():
    plays = Play.objects.all()
    return locals()

@register.inclusion_tag('partials/search.html')
def search():
    form = FilmSearchForm()
    return locals()

def _search_results(request):
    form = FilmSearchForm(request.GET)
    if form.is_valid():
        return form.search().distinct()
    return None

@register.inclusion_tag('partials/search_result.html', takes_context=True)
def search_result(context):
    films = _search_results(context['request'])
    if films:
        return {'films': films}

@register.inclusion_tag('partials/search_result.html', takes_context=True)
def search_result_adaptations(context):
    films = _search_results(context['request'])
    return {'films': Film.objects.query_adaptations(films)}

@register.inclusion_tag('partials/search_result.html', takes_context=True)
def search_result_references(context):
    films = _search_results(context['request'])
    return {'films': Film.objects.query_references(films)}

