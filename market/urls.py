from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('market.views',
    url(r'^$', 'product_list', name='product-list'),
)

