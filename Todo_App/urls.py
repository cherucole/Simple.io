from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.homepage, name='homepage'),
    url(r'^item/(?P<id>\d+)', views.item, name='item'),
    url(r'^item/(?P<id>\d+)/delete', views.item_delete, name='delete_item'),
    url(r'^add', views.add_item, name='add_item')

    # url(r'^details/item/(\d+)', views.item, name='item')

]
