# -*- coding: utf-8 -*- 
from annoying.decorators import render_to
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.conf import settings
from models import Gallerie

@render_to("gallerie/gallerie.html")
def gallerie(request, slug):
    gallerie = Gallerie.objects.get(slug=slug)
    return {"gallerie": gallerie}
