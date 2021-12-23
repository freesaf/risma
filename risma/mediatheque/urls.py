#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    url(r'^$', categorie_list, name='categorie_list'),
    url(r'^(?P<slug>[-\w]+)/$', categorie_details, name='categorie_details'),
    url(r'^(?P<slug>[-\w]+)/images/$', image_list, name='image_list'),
    url(r'^(?P<slug>[-\w]+)/videos/$', video_list, name='video_list'),
    url(r'^videos/last/$', last_cat_media_list, {'type': 'video'}, name='last_cat_video_list'),
    url(r'^images/last/$', last_cat_media_list, {'type': 'image'}, name='last_cat_image_list'),
    url(r'^dossiers/images/$', image_categories_list, name='image_categories_list'),
)

