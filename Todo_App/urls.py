from django.conf.urls import url
from . import views

app_name = 'items'

urlpatterns = [
    url('^$', views.homepage, name='homepage'),
    url(r'^item/(?P<id>\d+)', views.item, name='item'),
    url(r'^item/(?P<id>\d+)/delete', views.item_delete, name='item_delete'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.todo_delete, name='todo_delete'),

    url(r'^add', views.add_item, name='add_item')

    # url(r'^details/item/(\d+)', views.item, name='item')

]
