#-*- coding: utf-8 -*-
from django.template import Library
from custom_flatpages.models import FlatPage

from classytags.core import Tag, Options
from classytags.arguments import Argument
from django.template import loader, Context
from django import template

register = Library()


@register.inclusion_tag('flatpages/tags/flatpages.html')
def get_pagestatiques(cat=None, template_name='flatpages/tags/flatpages.html'):    
    flatpages = FlatPage.objects.all().filter(categorie__nom=cat)   
    return locals()
 
#register.tag(get_pagestatiques)
#register.simple_tag(get_pagestatiques)

