from django.conf.urls.defaults import *
from django.conf import settings

# admin
from django.contrib import admin
admin.autodiscover()
# Static files
urlpatterns = patterns('',
    (r'^static_admin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^feincms_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.FEINCMS_ADMIN_MEDIA_LOCATION, 'show_indexes': True}
    ),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
)

# regular urls
urlpatterns += patterns('',
    url(r'^$', 'app.views.simplepage', name='homepage'),
    url(r'^admin/', include(admin.site.urls)),
  #  (r'^search/', include('haystack.urls')),
    url(r'^(?P<slug>[-\w]+)/$', 'app.views.simplepage', name='simplepage'),
)

# specific urls
urlpatterns += patterns('',
    url(r'^films-description/(\d+)/$', 'filmography.views.film_description', name='film_description'),
    url(r'^films-quotation/(\d+)/$', 'filmography.views.film_quotation', name='film_quotation'),
    url(r'^films/(?P<slug>[-\w]+)/$', 'filmography.views.film', name='film'),
    url(r'^contributors/(?P<slug>[-\w]+)/$', 'filmography.views.contributor', name='contributor'),
    url(r'^plays/(?P<slug>[-\w]+)/films/$', 'filmography.views.play_films', name='play_films'),
    url(r'^analysis/(?P<slug>[-\w]+)/$', 'filmography.views.analysis', name='analysis'),
)


# Preview errors in local
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^404$', handler404),
        (r'^500$', handler500),
    )
