from django.conf.urls.defaults import *
from django.contrib import admin

from models import Popup

admin.autodiscover()

urlpatterns = patterns('popup.views',
    url(r'^$', 'liste_popups',name='liste_popups'),
    )