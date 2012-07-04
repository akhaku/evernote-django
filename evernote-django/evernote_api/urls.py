from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^oauth/', 'evernote_api.views.get_evernote_token'),
)
