"""Urls for the Zinnia entries"""
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

from zinnia.models import Entry
from zinnia.settings import PAGINATION
from zinnia.settings import ALLOW_EMPTY
from zinnia.settings import ALLOW_FUTURE

entry_conf_index = {#'paginate_by': PAGINATION,
                    'template_name': 'zinnia/entry_archive.html'}

entry_conf = {'date_field': 'creation_date',
              'allow_empty': ALLOW_EMPTY,
              'allow_future': ALLOW_FUTURE,
              'month_format': '%m'}

entry_conf_year = entry_conf.copy()
entry_conf_year['make_object_list'] = True
del entry_conf_year['month_format']

entry_conf_detail = entry_conf.copy()
del entry_conf_detail['allow_empty']
entry_conf_detail['queryset'] = Entry.published.all()


urlpatterns = patterns(
    'zinnia.views.entries',
    url(r'^$',
        'entry_index', entry_conf_index,name='zinnia_entry_archive_index'),
    url(r'^page/(?P<page>\d+)/$','entry_index', entry_conf_index,name='zinnia_entry_archive_index_paginated'),
    url(r'^(?P<year>\d{4})/$','entry_year', entry_conf_year,name='zinnia_entry_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$','entry_month', entry_conf,name='zinnia_entry_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$','entry_day', entry_conf,name='zinnia_entry_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$','entry_detail', entry_conf_detail, name='zinnia_entry_detail'),
    url(r'^(?P<object_id>\d+)/$', 'entry_shortlink',name='zinnia_entry_shortlink'),
    url(r'^entry_visit_count/(?P<entry_id>\d+)/$', 'entry_visit_count',  name='entry_visit_count')
    )
