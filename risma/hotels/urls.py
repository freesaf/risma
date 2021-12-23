#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    url(r'^hotel/(?P<slug>[-\w]+)/$', hotel_detail, name='hotel_detail'),
)
