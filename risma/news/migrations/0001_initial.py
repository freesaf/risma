# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'News'
        db.create_table('news_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('contenu', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from=None, unique_with=(), db_index=True)),
        ))
        db.send_create_signal('news', ['News'])


    def backwards(self, orm):
        
        # Deleting model 'News'
        db.delete_table('news_news')


    models = {
        'news.news': {
            'Meta': {'object_name': 'News'},
            'contenu': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['news']
