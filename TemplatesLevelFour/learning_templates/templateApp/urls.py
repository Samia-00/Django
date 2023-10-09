from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from templateApp import views

app_name = 'templateApp'

urlpatterns = [
    url(r'^relative/$', views.relative,name = 'relative'),
    url(r'^other/$', views.other,name = 'other'),
]