from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^create/$', 'fithack.views.create_group', name='create_group'),
    url(r'^group/(?P<group_id>\w+)/$', 'fithack.views.group', name='group'),
    url(r'^user_dashboard/$', 'fithack.views.user_dashboard', name='user_dashboard'),
    url(r'^admin/', include(admin.site.urls)),
)
