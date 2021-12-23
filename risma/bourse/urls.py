#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from django.views.generic.create_update import create_object, update_object, delete_object
from django.views.generic.list_detail import object_list

from models import *
from views import *


urlpatterns = patterns('',
    url(r"^graphe/$", graphe, name="graphe"),
    #url(r"^indicateur/$", indicateur, name="indicateur"),
)