from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hotel_list, name='hotel_list'),
    url(r'^hotel/(?P<pk>\d+)/$', views.hotel_detail, name='hotel_detail'),

]
