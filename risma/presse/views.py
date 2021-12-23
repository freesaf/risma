#-*- coding: utf-8 -*-
from annoying.decorators import render_to
from django.shortcuts import get_object_or_404
from models import CommuniquePresse

@render_to('presse/communique_details.html')
def communique_details(request, slug):
    presse = get_object_or_404(CommuniquePresse, slug=slug)
    return {'presse': presse}   
    
@render_to('presse/communique.html')
def communique(request):
    presse = CommuniquePresse.objects.all().order_by("-date")
    return {'presse': presse}