from django import template
from app.models import SimplePage
from django.core.urlresolvers import reverse

register = template.Library()
   
    
@register.simple_tag
def link(reference, args=""):
    """
    Generates a url to a SimplePage object by its reference
    ex : {% link page_reference %}
    """
    try:
        page = SimplePage.objects.filter(reference=reference)[0]
    except IndexError:
        raise SimplePage.DoesNotExist("No page with reference\"%s\" was found." % reference)
        return ''
    if args != '':
        args = '?'+str(args).replace(' ', '').replace(',', '&')
    
    return reverse('simplepage', None, None, {'slug': page.slug})+args
    