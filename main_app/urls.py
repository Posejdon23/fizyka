from django.conf.urls import url
from main_app.views import MainView

from . import views

app_name = "main_app"
urlpatterns = [
    url(r'^$', MainView.as_view(), name = 'main'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^login/$', views.log_me_in, name = 'login'),
]