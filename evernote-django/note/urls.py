from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url('^notes/$', 'note.views.home'),
)
