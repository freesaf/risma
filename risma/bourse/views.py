#-*- coding: utf-8 -*-
from annoying.decorators import render_to
from django.contrib import messages
from django.shortcuts import get_object_or_404, get_list_or_404, render_to_response
from django.http import HttpResponseRedirect
import datetime
from dateutil.relativedelta import relativedelta
from django.conf import settings
from risma.bourse.models import *
import time

@render_to("bourse/graphe.html")
def graphe(request):
    today= datetime.date.today()
    trimestre = today - relativedelta(days = -5)
    cours= Cour.objects.all()

    return locals()

"""@render_to("bourse/indicateur.html")
def indicateur(request):
    indicateur= Indicator.objects.all().order_by('-id')[:0]
    return indicateur"""