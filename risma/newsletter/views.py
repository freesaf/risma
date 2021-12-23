#-*- coding: utf-8 -*-
from annoying.decorators import render_to

from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from forms import NewsletterForm

@render_to("newsletter/form.html")
def register(request):
    if request.POST:
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, u"Inscription effectuée avec succès")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
        else:
            messages.error(request, u"Adresse email non valide!")
            return HttpResponseRedirect('/')
    else: 
        form = NewsletterForm()
    return {"form": form}
