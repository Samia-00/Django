from django.conf.urls import url,include
from firstApp import views

urlpatterns = [
    url(r'^$',views.index,name='index'),

]
