#-*- coding: utf-8 -*-
import csv
from django.contrib import admin
from models import Email
from django.http import HttpResponse
from custom_admin.export_csv import queryset_to_csv


def import_contact(modeladmin, request, queryset):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=newsletter.csv'
    writer = csv.writer(response)
    for contact in Email.objects.all():
        writer.writerow([contact.email])
    return response
import_contact.short_description = "Importer tous les emails"


class NewsletterAdmin(admin.ModelAdmin):
    search_fiels = ["email"] 
    actions = [import_contact]
    
admin.site.register(Email, NewsletterAdmin)

