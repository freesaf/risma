#-*- coding: utf-8 -*-
from django.template import Library
from presse.models import CommuniquePresse

register = Library()

@register.inclusion_tag('presse/tags/presse_list.html')
def presse_list(count=3):
    """
        {% presse_list [number]  %}
    """
    presse_list = CommuniquePresse.objects.all()[:count]
    return locals()

