from django.contrib import admin
from django import forms
from models import *
from lib.utils.form import fields_label, fields_help
from filebrowser.fields import FileBrowseWidget
from assetsmanager import manager

class CustomAdmin(admin.ModelAdmin):
    class Media:
        js = manager.get_assets_for_bundle_name('admin.form', 'js')


class ActorsInline(admin.TabularInline):
    verbose_name = "actor"
    verbose_name_plural = "actors"
    model = FilmCharacter
    extra = 1


class EnumReferenceAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EnumReferenceAdminForm, self).__init__(*args, **kwargs)
        fields_help(self.fields, {
            'name': "Visible label",
            'reference': "System internal name - webmaster only, don't change this -",
        })
        

class EnumReferenceAdmin(admin.ModelAdmin):
    form = EnumReferenceAdminForm
    ordering = ('name',)

class ContributorAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContributorAdminForm, self).__init__(*args, **kwargs)
        fields_help(self.fields, {
            'image': "Width: 120px, height: 90px"
        })
        
    class Meta:
        widgets = {
            'image': FileBrowseWidget({})
        }

######################

# Basic enum value references

admin.site.register(CharacterRole, EnumReferenceAdmin)
admin.site.register(FilmType, EnumReferenceAdmin)
admin.site.register(FilmMedium, EnumReferenceAdmin)
admin.site.register(Play, EnumReferenceAdmin)
admin.site.register(PlayReferenceType, EnumReferenceAdmin)

######################

class ContributorAdmin(CustomAdmin):
    form = ContributorAdminForm
    list_display = ('fullname', 'position',)
    ordering = ('position',)
    
admin.site.register(Contributor, ContributorAdmin)

####################

class CharacterAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CharacterAdminForm, self).__init__(*args, **kwargs)
        fields_help(self.fields, {
            'roles': "Select roles that this person may have",
            'firstname': "Or nickname",
        })
    
    class Meta:
        widgets = {
            'roles': forms.widgets.CheckboxSelectMultiple(),
        }
        

class CharacterAdmin(admin.ModelAdmin):
    form = CharacterAdminForm
    list_display = ('fullname_reversed',)
    ordering = ('lastname',)
    list_filter = ('roles__name',)

admin.site.register(Character, CharacterAdmin)

####################

class FilmAdminForm(forms.ModelForm):
    
    directors = forms.ModelMultipleChoiceField(queryset=Character.objects.filter(roles__reference='director'))
    cinematographers = forms.ModelMultipleChoiceField(queryset=Character.objects.filter(roles__reference='cinematographer'))
    editors = forms.ModelMultipleChoiceField(queryset=Character.objects.filter(roles__reference='editor'))
    musicians = forms.ModelMultipleChoiceField(queryset=Character.objects.filter(roles__reference='musician'))
    designers = forms.ModelMultipleChoiceField(queryset=Character.objects.filter(roles__reference='designer'))
    costume_designers = forms.ModelMultipleChoiceField(queryset=Character.objects.filter(roles__reference='costume-designer'))
    producers = forms.ModelMultipleChoiceField(queryset=Character.objects.filter(roles__reference='producer'))
    scriptwriters = forms.ModelMultipleChoiceField(queryset=Character.objects.filter(roles__reference='scriptwriter'))
    
    def __init__(self, *args, **kwargs):
        super(FilmAdminForm, self).__init__(*args, **kwargs)
        fields_help(self.fields, {
            'length': "Time in minutes",
            'countries': "List of countries in iso format, 2 letters comma separated. ex: fr, gb, de - Codes here : http://www.iso.org/iso/english_country_names_and_code_elements",
            'languages': "List of languages in iso format, 2 letters comma separated. ex: fr, en, de - Codes here : http://hapax.qc.ca/iso639-2.fr.htm",
            'is_color': "Check this if a colored version exists",
            'contributor': "Contributor responsible for this form",
        })
        fields_label(self.fields, {
            'publish_date': "Year or publication",
            'release_date': "Year of release",
            'is_color': "Available in color",
            'body': "Synopsis",
        })

class FilmAdmin(CustomAdmin):
    form = FilmAdminForm
    inlines = (ActorsInline,)
    ordering = ('title_fr',)
    
admin.site.register(Film, FilmAdmin)

####################

class AnalysisAdmin(CustomAdmin):
    pass

admin.site.register(Analysis, AnalysisAdmin)

####################

class PlayReferenceAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlayReferenceAdminForm, self).__init__(*args, **kwargs)

class PlayReferenceAdmin(CustomAdmin):
    form = PlayReferenceAdminForm
    list_display = ('__str__', 'type')
    list_filter = ('type', 'play')

admin.site.register(PlayReference, PlayReferenceAdmin)