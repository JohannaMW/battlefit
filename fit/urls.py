from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'fithack.views.home', name='home'),
    url(r'^user_dashboard/$', 'fithack.views.user_dashboard', name='user_dashboard'),

    # ajax
    url(r'^new_calories_consume/$', 'fithack.views.new_calories_consume', name='new_calories_consume'),
    url(r'^new_calories_burned/$', 'fithack.views.new_calories_burned', name='new_calories_burned'),
    url(r'^new_body_fat/$', 'fithack.views.new_body_fat', name='new_body_fat'),


    url(r'^admin/', include(admin.site.urls)),
)
