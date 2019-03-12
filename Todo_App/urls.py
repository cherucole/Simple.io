from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.homepage, name='homepage'),
    url(r'^details/item/(?P<id>\d+)', views.item, name='item')
    # url(r'^details/item/(\d+)', views.item, name='item')


]
