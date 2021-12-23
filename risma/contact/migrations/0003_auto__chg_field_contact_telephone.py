# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Contact.telephone'
        db.alter_column('contact_contact', 'telephone', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))


    def backwards(self, orm):
        
        # Changing field 'Contact.telephone'
        db.alter_column('contact_contact', 'telephone', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True))


    models = {
        'contact.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'organisation': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'sujet': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'})
        }
    }

    complete_apps = ['contact']
