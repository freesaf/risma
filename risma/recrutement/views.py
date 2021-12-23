# -*- coding: utf-8 -*- 
from annoying.decorators import render_to
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from datetime import date

from models import Offre
from forms import RecrutementForm


@render_to("recrutement/offre_list.html")
def offre_list(request):
    offres = Offre.objects.filter(date_de_cloture__gt = date.today() ).order_by('date_de_cloture') 
    return locals()

@render_to("recrutement/offre_detail.html")
def offre_detail(request,object_id=None):
    offre = Offre.objects.get(id=object_id)
    return locals()

@render_to("recrutement/recrutement.html")
def recrutement(request,object_id=None):
    if request.POST:
        form = RecrutementForm(request.POST, request.FILES)
        if form.is_valid():
            #form.offre.id = object_id
            form.save()
            messages.success(request, u'Formulaire envoyé avec succès.')
            return HttpResponseRedirect(reverse("index"))
    else:
         form = RecrutementForm()
    return {"form": form}   

