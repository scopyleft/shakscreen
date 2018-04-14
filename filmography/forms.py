# -*- coding: utf-8 -*-

from django import forms
from lib.utils import i10n
from filmography.models import Film, Play, Contributor, PlayReferenceType, Country
from django.db.models import Q

countries = i10n.countries()
countries_choices = [].append(countries)
print countries_choices

class FilmSearchForm(forms.Form):
    title = forms.CharField()
    character = forms.CharField(label="People (director, actor, etc.)")
    country = forms.ChoiceField()
    start_date = forms.IntegerField(label="Year(s) from ")
    end_date = forms.IntegerField(label="to")
    play = forms.ModelChoiceField(label="Shakespeare Play", queryset=Play.objects.all())
    adaptation = forms.ModelChoiceField(label="Adaptation/Allusion/Reference", queryset=PlayReferenceType.objects.all(), widget=forms.RadioSelect())
    contributor = forms.ModelChoiceField(queryset=Contributor.objects.all())
    
    def __init__(self, *args, **kwargs):
        super(FilmSearchForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].required = False
        self.fields['title'].widget.attrs = {'autocomplete': 'off'}
        self.fields['character'].widget.attrs = {'autocomplete': 'off'}
        self.fields['start_date'].widget.attrs = {'autocomplete': 'off'}
        self.fields['end_date'].widget.attrs = {'autocomplete': 'off'}
        self.fields['country'].choices = (('',''),)+Country.objects.all()
    
    def search(self):
        """@return film query (not the result set!)"""
        datas = self.cleaned_data
        films = Film.objects
        if datas['title']:
            films = films.filter(Q(title_fr__icontains=datas['title']) | Q(title_en__icontains=datas['title']))
        if datas['character']:
            films = films.filter(Q(actors__firstname__icontains=datas['character']) | Q(actors__lastname__icontains=datas['character']))
        if datas['country']:
            films = films.filter(countries__icontains=datas['country'])
        if datas['start_date']:
            films = films.filter(release_date__gte=datas['start_date'])
        if datas['end_date']:
            films = films.filter(release_date__lte=datas['end_date'])
        if datas['play']:
            films = films.filter(play_references__play=datas['play'])
        if datas['adaptation']:
            films = films.filter(play_references__type__name=datas['adaptation'])
        if datas['contributor']:
            films = films.filter(contributor=datas['contributor'])
        return films
    
"""
Title: champ libre [le moteur de recherche doit pouvoir retrouver un titre sans tenir compte des majuscules et à partir d'une partie du titre; le champ doit alors suggérer plusieurs titres: je tape "enfants", 2 titres apparaissent: "Enfants du paradis (Les)" et "Enfants du siècle (Les)" dans un sous champ; je sélectionne le titre que je veux]
"People" (director, actor, etc.): champ libre [le moteur de recherche doit pouvoir retrouver un nom sans tenir compte des majuscules et à partir d'une partie du nom, voire du prénom; le champ doit alors suggérer plusieurs noms: je tape "andré", 2 noms apparaissent: "André Hunnebelle" et "André Barsacq" dans un sous champ; je sélectionne le nom que je veux]
Country [champ avec liste prédéfinie menu déroulant]
Year(s) [période entre 2 dates: 2 champs dates séparés par "to"]
Shakespeare Play [champ avec liste prédéfinie menu déroulant]
Adaptation / Reference / Allusion [bouton radio ou champ avec liste prédéfinie menu déroulant]
Contributor [champ avec liste prédéfinie menu déroulant]
"""