#-*- coding: utf-8 -*-
from annoying.decorators import render_to
from django.shortcuts import get_object_or_404
from models import Hotel

@render_to("hotel/hotel_detail.html")
def hotel_detail(request, slug):
    hotels = get_object_or_404(Hotel, slug=slug)
    return {"hotel": hotels}
