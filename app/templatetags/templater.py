# -*- coding: utf-8 -*-

from django import template
from django.conf import settings

import re

register = template.Library()


@register.tag(name="evaluate")
def do_evaluate(parser, token):
    """
    Treats a string as a template and renders variables, templatestags, filters, …
    tag usage {% evaluate text %}
    """
    try:
        tag_name, variable = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]
    return EvaluateNode(variable)

class EvaluateNode(template.Node):
    def __init__(self, variable):
        self.variable = template.Variable(variable)

    def render(self, context):
        try:
            content = self.variable.resolve(context)
            content = convert_urls(content)
            t = template.Template(content)
            return t.render(context)
        except template.VariableDoesNotExist, template.TemplateSyntaxError:
            return 'Error evaluating "%s"' % self.variable


@register.filter
def tinymce_clean(text):
    """Removes beginning and trailing <p> tags"""
    return re.sub("(^<p>|</p>$)", "", text)


@register.filter
def convert_urls(value):
    """
    Replaces all href="@xxx" where xxx is a SimplePage reference by its url
    """
    import re
    def reference_to_url(ref):
        from app.models import SimplePage
        try:
            page = SimplePage.objects.filter(reference=ref.groups()[0])[0]
            url = page.url
        except IndexError:
            url = ''
        return 'href="%s"' % url
    return re.sub(r'href="@(\w+)"', reference_to_url, value)
