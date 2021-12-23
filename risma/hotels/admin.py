#-*- coding: utf-8 -*-
from django.contrib import admin
from models import Hotel

class HotelAdmin(admin.ModelAdmin):
    list_display = ('nom','slug')
    list_filter = ('nom',)
admin.site.register(Hotel, HotelAdmin)