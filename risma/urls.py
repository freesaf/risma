#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'index.html'}, name="index"),
    
    (r'^blog/', include('zinnia.urls')),  
    (r'^contact/', include('contact.urls')),
    (r'^documents/', include('file_uploader.urls', app_name="fichier", namespace="fichier")),
    (r'^gallerie/', include('gallerie.urls')),
    (r'^mediatheque/', include('mediatheque.urls', app_name="mediatheque", namespace="mediatheque")),
    (r'^news/', include('news.urls')),
    (r'^newsletter/', include('newsletter.urls')),
    (r'^presse/', include('presse.urls')),
    (r'^recrutement/', include('recrutement.urls')),
    (r'^popup/', include('popup.urls')),
    (r'^hotels/', include('hotels.urls')),
    (r'^bourse/', include('bourse.urls')),
    url(r'^confirmation_page$', direct_to_template, {'template': 'confirmation_page.html'}, name="confirmation_page"),
    url(r'^page$', direct_to_template, {'template': 'static/page.html'}, name="page"),
	url(r'^sitemap.xml$', direct_to_template, {'template': 'sitemap.xml'}, name="sitemap.xml"),
	(r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    
    (r'^admin/', include(admin.site.urls)),
    (r'^(?P<url>.*)$', 'custom_flatpages.views.flatpage'),
    (r'^ckeditor/', include('ckeditor.urls')),
    #(r'^sentry/', include('sentry.web.urls')),
)
