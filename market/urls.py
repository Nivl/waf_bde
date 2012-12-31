from django.conf.urls import patterns, url

urlpatterns = patterns('market.views',
    url(r'^$', 'product_list', name='product-list'),
)

