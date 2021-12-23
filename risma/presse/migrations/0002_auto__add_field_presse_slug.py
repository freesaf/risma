# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Presse.slug'
        db.add_column('presse_presse', 'slug', self.gf('autoslug.fields.AutoSlugField')(default=1, unique_with=(), max_length=50, populate_from=None, db_index=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Presse.slug'
        db.delete_column('presse_presse', 'slug')


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
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['presse']
