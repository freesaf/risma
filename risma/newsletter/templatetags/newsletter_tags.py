#-*- coding: utf-8 -*-
from classytags.core import Tag, Options
from classytags.arguments import Argument
from classytags.helpers import InclusionTag
from django import template
from django.template import RequestContext
from newsletter.forms import NewsletterForm as NF

register = template.Library()

class NewsletterForm(InclusionTag):
    name = 'newsletter'
    template = 'newsletter/included_form.html'
    
    def get_context(self, context):
        form = NF()
        context["newsletter_form"] = form
        return context
    
register.tag(NewsletterForm)