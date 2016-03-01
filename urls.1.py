from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = "main_app"
urlpatterns = [
    url(r'^$', views.main, name = 'main'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^login/$', views.logme, name = 'login'),
    url(r'^profile/$', views.profile, name = 'profile'),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', views.logoutme, name = 'logout'),
    url(r'^volumes/$', views.volumes, name = 'volumes'),
    url(r'^chapters/(?P<chapter_id>[0-9]+)/$', views.chapters, name='chapters'),
    url(r'^exercises/(?P<exercise_id>[0-9]+)/$', views.exercises, name='exercises'),
]