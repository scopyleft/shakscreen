from django.db import models
from django.template.defaultfilters import slugify
import re
import mptt

class SimplePage(models.Model):
    name = models.CharField(max_length=30)
    reference = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, blank=True)
    body = models.TextField()
    
    def __unicode__(self):
        return self.name
    
    def save(self):
        if not self.slug:
            self.slug = self.title
        self.slug = slugify(self.slug)
        return super(SimplePage, self).save()
    
    class Meta:
        ordering = ['name']
    
    @property
    @models.permalink
    def url(self):
        return ('simplepage', (), {'slug': self.slug})
    
    @property
    def navigation(self):
        """
        Return the first navigation object linked to the this Page
        """
        navigations = self.navigations
        if len(navigations) > 0:
            return navigations[0]
    
    @property
    def navigations(self):
        """
        Return all navigation objects linked to the this Page
        """
        return Navigation.objects.filter(page=self)


class Navigation(models.Model):
    title = models.CharField(max_length=50, blank=True)
    reference = models.CharField(max_length=30, blank=True)
    page = models.ForeignKey('SimplePage', blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    
    def __unicode__(self):
        return self.title
    
    def get_breadcrumb(self, include_self=True, min_level=0):
        ancestors = self.get_ancestors()
        breadcrumb = []
        for ancestor in ancestors:
            if ancestor.level >= min_level:
                breadcrumb.append(ancestor)
        if(include_self):
            breadcrumb.append(self)
        return breadcrumb
    
    class Meta:
        ordering = ['tree_id', 'lft']

mptt.register(Navigation)