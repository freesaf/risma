#-*- coding: utf-8 -*-
from annoying.decorators import render_to

from models import Popup


@render_to('popup/liste.html')  
def liste_popups (request):    
    list = Popup.objects.all()
    return {'list':list}