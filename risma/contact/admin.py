#-*- coding: utf-8 -*-
import csv
from django.contrib import admin
from django.http import HttpResponse

from custom_admin.export_csv import queryset_to_csv
from models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom','sujet','date_envoi')
    actions = [queryset_to_csv]
    csv_fields = (('id', 'id'), 
                  ('organisation', 'organisation'),
                  ('sujet', 'sujet'),
                  ('email', 'email'),
                  ('telephone', 'telephone'),
                  ('message', 'message'))
    csv_queryset = Contact.objects.all()
    
    def export_csv(self, request, queryset):
        opts = self.model._meta
        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(opts).replace('.', '_')
        writer = csv.writer(response)
        field_names = [field.name for field in opts.fields]
        # Write a first row with header information
        writer.writerow(field_names)
        # Write data rows
        for obj in queryset:
            writer.writerow([u"%s" % getattr(obj, field) for field in field_names])
        return response
    export_csv.short_description = u'Export CSV'
admin.site.register(Contact, ContactAdmin)