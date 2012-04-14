from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url('^logout/$', 'account.views.logout_page'),
    url('^auth/$', 'account.views.auth'),
)

