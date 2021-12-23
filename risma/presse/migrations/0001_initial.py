# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Presse'
        db.create_table('presse_presse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('extrait', self.gf('django.db.models.fields.TextField')()),
            ('media', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('diffusion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lien', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('fichier', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('presse', ['Presse'])


    def backwards(self, orm):
        
        # Deleting model 'Presse'
        db.delete_table('presse_presse')


    models = {
        'presse.presse': {
            'Meta': {'object_name': 'Presse'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'diffusion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'extrait': ('django.db.models.fields.TextField', [], {}),
            'fichier': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lien': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'media': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['presse']
