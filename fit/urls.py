from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^create/$', 'fithack.views.create_group', name='create_group'),
    url(r'^admin/', include(admin.site.urls)),
)
