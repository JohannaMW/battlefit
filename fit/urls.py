from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^create/$', 'fithack.views.create_group', name='create_group'),
    url(r'^group/(?P<group_id>\w+)/$', 'fithack.views.group', name='group'),

    url(r'^admin/', include(admin.site.urls)),
)
