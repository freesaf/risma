#-*- coding: utf-8 -*-
from django.template import Library
from recrutement.models import Offre

from classytags.core import Tag, Options
from classytags.arguments import Argument
from django.template import loader, Context
from django import template

from datetime import datetime


register = Library()


@register.inclusion_tag('recrutement/tags/offres.html')
def get_offres(nbr=3,template_name='recrutement/tags/offres.html'):    
    offres = Offre.objects.all()[:3]
    return {"offres": offres}
