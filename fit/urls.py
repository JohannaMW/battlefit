from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'fithack.views.home', name='home'),
    url(r'^user_dashboard/$', 'fithack.views.user_dashboard', name='user_dashboard'),

    url(r'^admin/', include(admin.site.urls)),
)
