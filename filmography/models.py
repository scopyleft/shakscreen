# -*- coding: utf-8 -*-

from filebrowser.fields import FileBrowseField
from django.db import models
from django.db.models import Q
from django.template.defaultfilters import slugify, striptags


class ContributorManager(models.Manager):
    def get_query_set(self):
        """
        Default order by position
        """
        return super(ContributorManager, self).get_query_set().order_by('position')

class Contributor(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.CharField(max_length=50, null=False, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    image = models.CharField(max_length=255)
    body = models.TextField()
    position = models.IntegerField(blank=True, default=1)
    slug = models.SlugField(blank=True)
    
    objects = ContributorManager()
    
    @property
    def fullname(self):
        return u"%s %s" % (self.firstname, self.lastname)
    
    def __unicode__(self):
        return self.fullname
    
    def save(self):
        if not self.slug:
            self.slug = '%s-%d' % (self.fullname, self.id)
        self.slug = slugify(self.slug)
        return super(Contributor, self).save()
    
    
#################
    
class CharacterRole(models.Model):
    name = models.CharField(max_length=30)
    reference = models.SlugField(max_length=30)
    
    def __unicode__(self):
        return self.name
    
class Character(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30, null=True, blank=True)
    roles = models.ManyToManyField(CharacterRole)
    
    """
    WTF ???
    """
    def roles_list(self):
        l = []
        for r in self.roles.all():
            l.append(r.name)
        print l.join(',')
        return 'a, b'
    
    @property
    def fullname(self):
        return u"%s %s" % (self.firstname, self.lastname)
    
    @property
    def fullname_reversed(self):
        return u"%s %s" % (self.lastname, self.firstname)
    
    def __unicode__(self):
        return self.fullname
    
    class Meta:
        ordering = ('firstname',)

##################

class FilmMedium(models.Model):
    name = models.CharField(max_length=50)
    reference = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name


class FilmType(models.Model):
    name = models.CharField(max_length=50)
    reference = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name


class Play(models.Model):
    name = models.CharField(max_length=100)
    reference = models.CharField(max_length=30, null=True, blank=True)
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.name
    
    def save(self):
        if not self.slug:
            self.slug = '%s-%d' % (self.name, self.id)
        self.slug = slugify(self.slug)
        return super(Play, self).save()


class PlayReferenceType(models.Model):
    name = models.CharField(max_length=100)
    reference = models.CharField(max_length=30, null=True, blank=True)
    
    def __unicode__(self):
        return self.name

class FilmManager(models.Manager):
    def query_adaptations(self, q):
        return q.filter(play_references__type__reference='adaptation')
    
    def adaptations(self):
        return self.query_adaptations(self.get_query_set())
    
    def query_references(self, q):
        return q.filter(
                Q(play_references__type__reference='implicit') | 
                Q(play_references__type__reference='explicit')
        )
        
    def references(self):
        return self.query_adaptations(self.get_query_set())

class Film(models.Model):
    title_fr = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    title_aka = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    directors = models.ManyToManyField(Character, related_name='director_films')
    actors = models.ManyToManyField(Character, through='FilmCharacter', related_name='actor_films')
    cinematographers = models.ManyToManyField(Character, related_name='cinematographer_films')
    editors = models.ManyToManyField(Character, related_name='editor_films')
    musicians = models.ManyToManyField(Character, related_name='musician_films')
    designers = models.ManyToManyField(Character, related_name='designer_films')
    costume_designers = models.ManyToManyField(Character, related_name='costume_designer_films')
    producers  = models.ManyToManyField(Character, related_name='producer_films')
    scriptwriters  = models.ManyToManyField(Character, related_name='scriptwriter_films')
    production = models.CharField(max_length=255)
    length = models.IntegerField() 
    countries = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)
    release_date = models.IntegerField()
    publish_date = models.IntegerField(null=True, blank=True)
    mediums = models.ManyToManyField(FilmMedium)
    types = models.ManyToManyField(FilmType, related_name="films")
    publisher = models.CharField(max_length=255, null=True, blank=True)
    image = FileBrowseField(null=True, blank=True)
    body = models.TextField()
    is_color = models.BooleanField()
    contributor = models.ForeignKey(Contributor, related_name='films')
    create_date = models.DateField(blank=True, auto_now_add=True)
    update_date = models.DateField(blank=True, auto_now=True)
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.title_fr
    
    @property
    def languages_list(self):
        return [x.strip() for x in self.languages.split(',')]
    
    @property
    def countries_list(self):
        return [x.strip() for x in self.countries.split(',')]
    
    @property
    def director(self):
        """
        Retrieves the first Director as default
        """
        try:
            return self.directors.all()[0]
        except IndexError:
            return None
    
    @property
    def play_references_types(self):
        types = []
        for play_reference in self.play_references.all():
            name = play_reference.type.name
            if not name in types:
                types.append(name)
        return types
    
    def save(self):
        if not self.slug:
            self.slug = u'%s-%d' % (self.title_fr, self.id)
        self.slug = slugify(self.slug)
        return super(Film, self).save()
    
    objects = FilmManager()
    
    class Meta:
        ordering = ['slug', '-release_date']


class FilmCharacter(models.Model):
    film = models.ForeignKey(Film)
    character = models.ForeignKey(Character)
    nickname = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.nickname
    
    @property
    def fullname(self):
        return "%s (%s)" % (self.character.__unicode__(), self.nickname)


class Analysis(models.Model):
    films = models.ManyToManyField(Film, related_name='analyses')
    contributors = models.ManyToManyField(Contributor, related_name='analyses')
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField()
    
    @property
    def main_film(self):
        return self.films.all()[0] or None
    
    def __unicode__(self):
        return striptags(self.title)
    
    def save(self):
        if not self.slug:
            self.slug = u'%s-%d' % (self.title, self.id)
        self.slug = slugify(self.slug)
        return super(Analysis, self).save()


class PlayReferenceManager(models.Manager):
    use_for_related_fields = True
    
    def ordered_by_film(self):
        return self.get_query_set().order_by('film__title_fr')
    
    def ordered_by_film_date(self):
        return self.get_query_set().order_by('-film__release_date')
    
    def adaptations(self):
        return self.ordered_by_film_date().filter(type__reference='adaptation')
    
    def allusions(self):
        return self.ordered_by_film_date().filter(Q(type__reference='implicit') | Q(type__reference='explicit'))
    
    
class PlayReference(models.Model):
    play = models.ForeignKey(Play, related_name='film_references')
    film = models.ForeignKey(Film, related_name='play_references')
    type = models.ForeignKey(PlayReferenceType)
    description = models.TextField()
    quotation = models.TextField()
    
    objects = PlayReferenceManager()
    
    def __unicode__(self):
        return u"%s - %s" % (self.film.__unicode__(), self.play.__unicode__())
    

class Country():
    class Objects():
        def all(self):
            #values = Film.objects.all().values_list('countries')
            #[v[0] for v in values]
            return (('fr','fr'), ('it','it'), ('be','be'))
    objects = Objects()

"""
class Quotation(models.Model):
    films = models.ManyToManyField(Film)
    text = models.TextField()
    is_implicit = models.BooleanField()
    body = models.TextField()
"""
