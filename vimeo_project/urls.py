# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
urlpatterns = patterns('',
    url(r'^$','vimeouser.views.search_user'),
    url(r'^ajax-user-list$','vimeouser.views.ajax_user_list',name='user_list'),
    # Examples:
    # url(r'^$', 'vimeo_project.views.home', name='home'),
    # url(r'^vimeo_project/', include('vimeo_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT }),
)
