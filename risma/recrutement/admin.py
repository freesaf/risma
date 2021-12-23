#-*- coding: utf-8 -*-
from django.contrib import admin
from models import CV,Offre

admin.site.register(CV)

class OffreAdmin(admin.ModelAdmin):
    search_fields = ('nomposte',)
    list_display = ('nomposte', 'date_de_cloture','secteur_dactivite','localisation',)
    
admin.site.register(Offre,OffreAdmin)