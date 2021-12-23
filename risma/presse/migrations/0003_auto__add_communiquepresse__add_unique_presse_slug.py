# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CommuniquePresse'
        db.create_table('presse_communiquepresse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('fichier', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from=None, unique_with=(), db_index=True)),
        ))
        db.send_create_signal('presse', ['CommuniquePresse'])

        # Adding unique constraint on 'Presse', fields ['slug']
        db.create_unique('presse_presse', ['slug'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Presse', fields ['slug']
        db.delete_unique('presse_presse', ['slug'])

        # Deleting model 'CommuniquePresse'
        db.delete_table('presse_communiquepresse')


    models = {
        'presse.communiquepresse': {
            'Meta': {'object_name': 'CommuniquePresse'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'fichier': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'presse.presse': {
            'Meta': {'object_name': 'Presse'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'diffusion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'extrait': ('django.db.models.fields.TextField', [], {}),
            'fichier': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lien': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'media': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['presse']
