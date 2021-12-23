#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    url(r'^revue-de-presse/$', communique, name="communique"),
    url(r'^revue-de-presse/(?P<slug>[-\w]+)/$', communique_details, name="communique_details"),

)