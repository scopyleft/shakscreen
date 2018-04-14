from haystack.indexes import *
from haystack import site
from filmography.models import Film


class FilmIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    title = CharField(model_attr='title')
    director = CharField(model_attr='director')

site.register(Film, FilmIndex)