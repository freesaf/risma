# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Contact.nom'
        db.add_column('contact_contact', 'nom', self.gf('django.db.models.fields.CharField')(default=1, max_length=250), keep_default=False)

        # Adding field 'Contact.organisation'
        db.add_column('contact_contact', 'organisation', self.gf('django.db.models.fields.CharField')(max_length=250, null=True), keep_default=False)

        # Adding field 'Contact.telephone'
        db.add_column('contact_contact', 'telephone', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Contact.nom'
        db.delete_column('contact_contact', 'nom')

        # Deleting field 'Contact.organisation'
        db.delete_column('contact_contact', 'organisation')

        # Deleting field 'Contact.telephone'
        db.delete_column('contact_contact', 'telephone')


    models = {
        'contact.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'organisation': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'sujet': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'telephone': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'})
        }
    }

    complete_apps = ['contact']
