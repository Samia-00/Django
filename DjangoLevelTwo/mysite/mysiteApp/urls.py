from django.conf.urls import url
from mysiteApp import views
urlpatterns = [
    url(r'^$', views.users, name='users'), # Comma was missing here
    # url(r'^$', views.help, name='help'), # Comma was missing here
]