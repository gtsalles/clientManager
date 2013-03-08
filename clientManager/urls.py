from django.conf.urls import patterns, include, url
from client import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'clientManager.views.home', name='home'),
    # url(r'^clientManager/', include('clientManager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #Client app urls
    url(r'^client/', views.create),
    url(r'^$', views.index),
    url(r'^address/', views.address),
)
