#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from views import *

urlpatterns = patterns('',
    
    url(r'^$', offre_list, name='offre_list'),
    url(r'^offre/(?P<object_id>\d+)$', offre_detail, name="offre_detail"),
    url(r'^postuler/(?P<object_id>\d+)$', recrutement, name="recrute"),
)

import signals