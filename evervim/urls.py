from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'edit.views.home'),
    url(r'^account/login/$', 'account.views.login_page'),
    url(r'^account/logout/$', 'account.views.logout_page'),
    url(r'^account/auth$', 'account.views.auth'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    # Examples:
)
