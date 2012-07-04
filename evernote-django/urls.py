from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'edit.views.home'),
    url(r'^edit/$', 'edit.views.edit_note'),
    url(r'^edit/(?P<guid>[\w-]+)/$', 'edit.views.edit_note'),
    url(r'^account/', include('account.urls')),
    url(r'^evernote/', include('evernote_api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
