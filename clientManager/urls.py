from django.conf.urls import patterns, include, url
from django.views.static import serve
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
    url(r'^$', views.index),
    url(r'^client/$', views.create_client),
    url(r'^profile/(\d+)/$', views.profile),
    url(r'^client/edit/(\d+)/$', views.edit_client),
    url(r'^client/delete/(\d+)/$', views.delete_client),

    # Address
    url(r'^address/$', views.address),
    url(r'^list/$', views.list_addresses),
    url(r'^show-address/(\d+)/$', views.list_address),
    url(r'^address/edit/(\d+)/$', views.edit_address),
    url(r'^address/delete/(\d+)/$', views.delete_address),

    url(r'^export/$', views.export),
)