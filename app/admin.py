#-*- coding:utf-8 -*-

from django.contrib import admin
from app.models import SimplePage, Navigation
from django import forms
from lib.utils.form import fields_label, fields_help
from django.conf import settings
from feincms.admin import editor
from assetsmanager import manager

class SimplePageAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SimplePageAdminForm, self).__init__(*args, **kwargs)
        fields_label(self.fields, {
            'name':  'nom',
            'title': 'titre',
            'body':  'Contenu',
        })
        fields_help(self.fields, {
             'name': "Nom de page. Uniquement pour l'organisation personnelle de l'administrateur",
             'title': 'Titre de la page. Apparait dans le navigateur (référencement +++)',
             'description': 'Description de la page. Apparait dans les moteurs de recherche (référencement +)',
             'slug': "Adresse dans l'url. (référencement ++)",
             'body': "Contenu de la page.",
             'reference': "Reference de page (utilisée pour les liens internes et pour reconnaitre la 'homepage')"                    
        })

class SimplePageAdmin(admin.ModelAdmin):
    form = SimplePageAdminForm
    fieldsets = (
        (None, {'fields': ('name',)}),
        ('Meta', {'fields': ('title', 'description', 'slug', 'reference')}),
        ('Contenu', {'fields': ('body',)}),
    )
    
    class Media:
        js = manager.get_assets_for_bundle_name('simplepage_form', 'js')

admin.site.register(SimplePage, SimplePageAdmin)



class NavigationAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NavigationAdminForm, self).__init__(*args, **kwargs)
        fields_label(self.fields, {
            'title': "Intitulé",
            'reference': "Nom de référence",
        })
        fields_help(self.fields, {
            'title': "Libellé affiché",
            'reference': "A renseigner pour un élément racine",
            'url': "lien absolu vers un site externe (http://…), au lieu d'une page interne",
            'page': "page à afficher",
        })
        

class NavigationAdmin(editor.TreeEditor):
    form = NavigationAdminForm
    def _actions_column(self, page):
        actions = super(NavigationAdmin, self)._actions_column(page)
        actions.insert(0, u'<a href="add/?parent=%s" title="%s"><img\
           src="%simg/admin/icon_addlink.gif" alt="%s"></a>' %
           (page.pk, u"Ajouter un élément ici",
           settings.ADMIN_MEDIA_PREFIX , u"Ajouter un élément ici"))
        return actions

    fieldsets = (
        (None, {'fields': ('title',)}),
        ('Lien', {'fields': ('page', 'url')}),
        ('Webmaster', {'fields': ('reference',)}),
        ('Position', {'fields': ('parent',), 'classes': ('collapsed',)}),
    )
    
admin.site.register(Navigation, NavigationAdmin)