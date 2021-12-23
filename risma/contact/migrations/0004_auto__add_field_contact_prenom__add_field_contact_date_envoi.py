# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Contact.prenom'
        db.add_column('contact_contact', 'prenom', self.gf('django.db.models.fields.CharField')(default='a', max_length=250), keep_default=False)

        # Adding field 'Contact.date_envoi'
        db.add_column('contact_contact', 'date_envoi', self.gf('django.db.models.fields.DateField')(auto_now_add=True, default=datetime.date(2012, 5, 30), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Contact.prenom'
        db.delete_column('contact_contact', 'prenom')

        # Deleting field 'Contact.date_envoi'
        db.delete_column('contact_contact', 'date_envoi')


    models = {
        'contact.contact': {
            'Meta': {'object_name': 'Contact'},
            'date_envoi': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'organisation': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'sujet': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'})
        }
    }

    complete_apps = ['contact']
