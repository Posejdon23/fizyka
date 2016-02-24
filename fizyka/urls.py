from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # url(r'^$', 'fizyka.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^main_app/', include('main_app.urls', namespace="main_app")),
    url(r'^admin/', include(admin.site.urls)),
]
