# from django.conf.urls import url

from basic_app import views
from django.urls import include, re_path
# from django.urls import include

app_name = 'basic_app'

urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^login/$', views.user_login, name='user_login'),
]
