# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Fichier.connexion_requise'
        db.add_column('file_uploader_fichier', 'connexion_requise', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Fichier.connexion_requise'
        db.delete_column('file_uploader_fichier', 'connexion_requise')


    models = {
        'file_uploader.fichier': {
            'Meta': {'object_name': 'Fichier'},
            'connexion_requise': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fichier': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['file_uploader']
