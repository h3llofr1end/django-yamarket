from django.conf.urls import url

from . import views

app_name = 'catalog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='catalog'),
    url(r'^(?P<product_id>[0-9]+)/$', views.product_page, name='detail'),
    url(r'^search/$', views.search, name='search')
]