from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'signapps.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', 'signapps.views.accounts', name='accounts'),
)