from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = "main_app"
urlpatterns = [
    url(r'^$', views.main, name = 'main'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^login/$', views.logme, name = 'login'),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', views.logoutme, name = 'logout'),
    url(r'^chapter_list/$', views.chapter_list, name = 'chapter_list'),
]