#-*- coding: utf-8 -*-
from annoying.decorators import render_to
from django.shortcuts import get_object_or_404
from models import News

@render_to("news/list.html")
def list(request):
    news = News.objects.all()
    return {"news": news}

@render_to("news/details.html")
def details(request, slug):
    news = get_object_or_404(News, slug=slug)
    return {"news": news}


