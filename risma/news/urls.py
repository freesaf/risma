#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from views import *

urlpatterns = patterns('',
    url(r'^$', list, name='news_list'),
    url(r'^(?P<slug>[-\w]+)$', details, name='news_details'),
)
