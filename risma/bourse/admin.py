#-*- coding: utf-8 -*-
from django.contrib import admin
from models import Cour, Indicator

"""class CoursAdmin(admin.ModelAdmin):
    list_display = ('date', 'dernier', 'premier', 'plus_haut', 'plus_bas', 'volume', 'capitaux', 'date_import')
    list_filter = ('date',)
admin.site.register(Cours, CoursAdmin)"""

class CourAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'dernier', 'premier', 'plus_haut', 'plus_bas', 'volume', 'capitaux', 'date_import')
    list_filter = ('date',)
admin.site.register(Cour, CourAdmin)

"""class IndicateurAdmin(admin.ModelAdmin):
    list_display = ('last_quote','currency', 'variation', 'curseur', 'date', 'isin', 'market_center' )
    list_filter = ('last_quote',)
admin.site.register(Indicateur, IndicateurAdmin)"""

class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_quote','currency', 'variation', 'curseur', 'date', 'isin', 'market_center' )
    list_filter = ('last_quote',)
admin.site.register(Indicator, IndicatorAdmin)