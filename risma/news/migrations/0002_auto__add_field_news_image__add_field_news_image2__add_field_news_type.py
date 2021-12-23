# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'News.image'
        db.add_column('news_news', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'News.image2'
        db.add_column('news_news', 'image2', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'News.type'
        db.add_column('news_news', 'type', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'News.image'
        db.delete_column('news_news', 'image')

        # Deleting field 'News.image2'
        db.delete_column('news_news', 'image2')

        # Deleting field 'News.type'
        db.delete_column('news_news', 'type')


    models = {
        'news.news': {
            'Meta': {'object_name': 'News'},
            'contenu': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['news']
