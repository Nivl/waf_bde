from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'waf_bde.views.home', name='home'),
    # url(r'^waf_bde/', include('waf_bde.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
