from django import template
from django.template.loader import render_to_string
from app.models import Navigation, SimplePage
from django.core.urlresolvers import resolve
from django.conf import settings

register = template.Library()


class MenuNode(template.Node):
    def __init__(self, menu_name):
        self.menu_name = menu_name
    def render(self, context):
        trees = Navigation.objects.filter(reference=self.menu_name)
        try:
            tree = trees[0].get_descendants()
        except IndexError:
            raise IndexError('Menu template error : no navigation has reference "%s"' % self.menu_name)
        breadcrumb = []
        try:
            url = resolve(context['request'].path)
            slug = url[2]['slug']
            try:
                page = SimplePage.objects.filter(slug=slug)[0]
                try:
                    current_nav = Navigation.objects.get(page=page.id)
                    breadcrumb = current_nav.get_breadcrumb()
                except:
                    pass
            except IndexError:
                pass
        except KeyError:
            print 'No navigation for url %s was found %s' % url
        finally:
            vars = locals()
            vars.update({'settings': settings})
            return render_to_string('menu.html', vars)
        


@register.tag()
def menu(parser, token):
    try:
        tag_name, menu_name = token.split_contents()
        # stip quotes if present
        if menu_name[0] in ('\'', '"') and menu_name[0] == menu_name[-1]:
            menu_name = menu_name[1:-1]
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires arguments" % token.contents.split()[0]
    return MenuNode(menu_name)
    

@register.inclusion_tag('partials/breadcrumb.html')
def breadcrumb(param=None):
    crumbs = []
    if isinstance(param, SimplePage):
        from django.core.urlresolvers import reverse
        # display navigation hierarchy
        if param.navigation:
            navigations = param.navigation.get_breadcrumb(min_level=1)
            for navigation in navigations:
                url = reverse('simplepage', args=[navigation.page.slug]) if navigation.page else navigation.url
                crumbs.append({'label': navigation.title, 'url': url})
        # page has no matching navigation, display page only
        # don't treat homepage
        elif param.reference != 'homepage':
            crumbs.append({'label': param.title, 'url': reverse('simplepage', args=[param.slug])})
    return {'crumbs': crumbs}

@register.simple_tag
def in_breadcrumb(breadcrumb, item):
    return 'current' if item in breadcrumb else ''