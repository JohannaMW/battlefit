from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
<<<<<<< HEAD
    # url(r'^$', 'fit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^create/$', 'fithack.views.create_group', name='create_group'),
    url(r'^group/(?P<group_id>\w+)/$', 'fithack.views.group', name='group'),
=======
    url(r'^$', 'fithack.views.home', name='home'),
    url(r'^user_dashboard/$', 'fithack.views.user_dashboard', name='user_dashboard'),

>>>>>>> 400276e8538284de924be0e7065fd97959519a05
    url(r'^admin/', include(admin.site.urls)),
)
