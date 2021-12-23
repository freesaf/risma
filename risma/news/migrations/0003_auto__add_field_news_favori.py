# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'News.favori'
        db.add_column('news_news', 'favori', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'News.favori'
        db.delete_column('news_news', 'favori')


    models = {
        'news.news': {
            'Meta': {'object_name': 'News'},
            'contenu': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'favori': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'texte'", 'max_length': '20', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['news']
