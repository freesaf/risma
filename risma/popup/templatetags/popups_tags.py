#-*- coding: utf-8 -*-
from django.template import Library
from popup.models import Popup

from classytags.core import Tag, Options
from classytags.arguments import Argument
from django.template import loader, Context
from django import template

from datetime import datetime


register = Library()

"""
@register.inclusion_tag('popup/tags/popup.html')
def display_popup( template_name='popup/tags/popup.html'):    
    popup = Popup.objects.all()
    return {"popup": popup}

"""

class display_popup(Tag):
    name = 'display_popup'
    options = Options(
        Argument('category', default="homepage", required=True, resolve=True),
        Argument('template_id', default="popup", required=False, resolve=False)
    )
    """
    utilisation : 
    {% block popup %}
        {% load popups_tags %}
            {% display_popup "homepage" "template_name" %}
    {% endblock %}
    pour le deuxieme parametre : sans préciser le chemin ni extension , c par defaut popup/tags
    """
    def render_tag(self, context, category, template_id):
        popup = Popup.objects.all().filter(date_debut__lte=datetime.now(),date_fin__gte=datetime.now())
        variables = Context({"popup": popup})
        return loader.get_template('popup/tags/%s.html' % template_id).render(variables)
    
register.tag(display_popup)