from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^oauth/', include('social_django.urls',
                            namespace='social')),  # for social login
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'', include('Todo_App.urls'))

]
