from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('waf_bde.views',
    url(r'^$', 'home', name='home'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^polls/', 'survey', name='survey'),
    url(r'^market/', include('market.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^crowdsourcing/', include('crowdsourcing.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.haml'}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
