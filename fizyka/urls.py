from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fizyka.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^main_app/', include('main_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
