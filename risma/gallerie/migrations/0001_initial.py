# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Gallerie'
        db.create_table('gallerie_gallerie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from=None, db_index=True)),
        ))
        db.send_create_signal('gallerie', ['Gallerie'])

        # Adding model 'Photo'
        db.create_table('gallerie_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('gallerie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallerie.Gallerie'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('gallerie', ['Photo'])


    def backwards(self, orm):
        
        # Deleting model 'Gallerie'
        db.delete_table('gallerie_gallerie')

        # Deleting model 'Photo'
        db.delete_table('gallerie_photo')


    models = {
        'gallerie.gallerie': {
            'Meta': {'object_name': 'Gallerie'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None', 'db_index': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'gallerie.photo': {
            'Meta': {'object_name': 'Photo'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'gallerie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallerie.Gallerie']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['gallerie']
