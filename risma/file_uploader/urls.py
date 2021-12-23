#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template  
from django.views.generic.list_detail import object_list

from views import *


fichier_list_conf = {
    'queryset': Fichier.publications.all().order_by('categorie', '-date') 
}

urlpatterns = patterns('',
    url(r'^$', object_list, fichier_list_conf, name="list"),
    url(r'^download/(?P<file_id>[0-9]+)/$', download, name="download"),
)