#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from views import *

urlpatterns = patterns('',
    url(r'^$', contact, name='contact'),
    url(r'^confirmation$', direct_to_template, {'template': 'contact/confirmation.html'}, name='contact-confirmation-envoi'),
)

import signals
