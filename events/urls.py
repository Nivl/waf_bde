from django.conf.urls import patterns, url

urlpatterns = patterns('events.views',
    url(r'^$', 'event_list', name='event-list'),
)

