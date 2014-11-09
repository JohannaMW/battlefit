from django.conf.urls import patterns, include, url
from django.contrib import admin
from fit import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^create/$', 'fithack.views.create_group', name='create_group'),
    url(r'^group/(?P<group_id>\w+)/$', 'fithack.views.group', name='group'),
    url(r'^user_dashboard/$', 'fithack.views.user_dashboard', name='user_dashboard'),
    # ajax
    url(r'^new_calories_consume/$', 'fithack.views.new_calories_consume', name='new_calories_consume'),
    url(r'^new_calories_burned/$', 'fithack.views.new_calories_burned', name='new_calories_burned'),
    # url(r'^new_body_fat/$', 'fithack.views.new_body_fat', name='new_body_fat'),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'fithack.views.home', name='home'),

    # register log in and out
    url(r'^register/$', 'fithack.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^profile/$', 'fithack.views.profile', name='profile'),

    #password reset
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),


)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
