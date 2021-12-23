# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Recrutement'
        db.create_table('recrutement_recrutement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('date_naissance', self.gf('django.db.models.fields.DateField')()),
            ('ville', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('cv', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('lettre_motivation', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('recrutement', ['Recrutement'])


    def backwards(self, orm):
        
        # Deleting model 'Recrutement'
        db.delete_table('recrutement_recrutement')


    models = {
        'recrutement.recrutement': {
            'Meta': {'object_name': 'Recrutement'},
            'cv': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_naissance': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lettre_motivation': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['recrutement']
