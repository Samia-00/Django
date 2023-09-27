
from django.conf.urls import url
from appTwo import views

urlpatterns = [
    # url(r'^$', views.index, name='index'), # Comma was missing here
    url(r'^$', views.help, name='help'), # Comma was missing here

]
