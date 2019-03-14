from django.conf.urls import url
from . import views

app_name = 'items'

urlpatterns = [
    url('^$', views.homepage, name='homepage'),
    url(r'^item/(?P<id>\d+)', views.item, name='item'),
    url(r'^delete/(?P<id>[0-9]+)/$', views.todo_delete, name='todo_delete'),
    url(r'^add', views.add_item, name='add_item'),
]
