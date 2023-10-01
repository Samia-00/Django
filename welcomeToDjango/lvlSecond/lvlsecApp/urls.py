from django.conf.urls import url
from lvlsecApp import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]