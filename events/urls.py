from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('events.views',
    url(r'^$', 'event_list', name='event-list'),
)

