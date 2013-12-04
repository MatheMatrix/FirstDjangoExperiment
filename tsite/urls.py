from django.conf.urls import patterns, include, url
from tsite.views import *
#import tsite.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    ('^$', love_jiajia),
    (r'^time/$', current_datetime),
    (r'^jiajia/', love_jiajia),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    # Examples:
    # url(r'^$', 'tsite.views.home', name='home'),
    # url(r'^tsite/', include('tsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
