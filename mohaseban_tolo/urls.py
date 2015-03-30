from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mohaseban_tolo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'mohaseban.views.main_page',name='home'),
    url(r'^adminmazdak/', include(admin.site.urls)),
)
