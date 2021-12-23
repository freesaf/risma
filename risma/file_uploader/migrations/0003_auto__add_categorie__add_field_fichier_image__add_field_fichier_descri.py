# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Categorie'
        db.create_table('file_uploader_categorie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('file_uploader', ['Categorie'])

        # Adding field 'Fichier.image'
        db.add_column('file_uploader_fichier', 'image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100), keep_default=False)

        # Adding field 'Fichier.description'
        db.add_column('file_uploader_fichier', 'description', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Fichier.categorie'
        db.add_column('file_uploader_fichier', 'categorie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['file_uploader.Categorie'], null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Categorie'
        db.delete_table('file_uploader_categorie')

        # Deleting field 'Fichier.image'
        db.delete_column('file_uploader_fichier', 'image')

        # Deleting field 'Fichier.description'
        db.delete_column('file_uploader_fichier', 'description')

        # Deleting field 'Fichier.categorie'
        db.delete_column('file_uploader_fichier', 'categorie_id')


    models = {
        'file_uploader.categorie': {
            'Meta': {'object_name': 'Categorie'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'file_uploader.fichier': {
            'Meta': {'object_name': 'Fichier'},
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['file_uploader.Categorie']", 'null': 'True', 'blank': 'True'}),
            'connexion_requise': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fichier': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['file_uploader']
