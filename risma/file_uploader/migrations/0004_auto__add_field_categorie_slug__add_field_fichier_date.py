# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Categorie.slug'
        db.add_column('file_uploader_categorie', 'slug', self.gf('autoslug.fields.AutoSlugField')(default=' ', unique_with=(), populate_from=None, max_length=50, unique=True, db_index=True), keep_default=False)

        # Adding field 'Fichier.date'
        db.add_column('file_uploader_fichier', 'date', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Categorie.slug'
        db.delete_column('file_uploader_categorie', 'slug')

        # Deleting field 'Fichier.date'
        db.delete_column('file_uploader_fichier', 'date')


    models = {
        'file_uploader.categorie': {
            'Meta': {'object_name': 'Categorie'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'})
        },
        'file_uploader.fichier': {
            'Meta': {'object_name': 'Fichier'},
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['file_uploader.Categorie']", 'null': 'True', 'blank': 'True'}),
            'connexion_requise': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fichier': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['file_uploader']
