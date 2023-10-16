# from django.conf.urls import url
from basic_app import views
from django.urls import include, re_path

app_name = 'basic_app'
urlpatterns = [
    re_path(r'^$', views.SchoolListView.as_view(), name = 'list'),
    re_path(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name = 'detail'),


]
