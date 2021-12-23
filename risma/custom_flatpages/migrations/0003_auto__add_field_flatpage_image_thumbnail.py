# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'FlatPage.image_thumbnail'
        db.add_column('custom_flatpages_flatpage', 'image_thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'FlatPage.image_thumbnail'
        db.delete_column('custom_flatpages_flatpage', 'image_thumbnail')


    models = {
        'custom_flatpages.categorie': {
            'Meta': {'object_name': 'Categorie'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'custom_flatpages.flatpage': {
            'Meta': {'ordering': "('ordre', 'url')", 'object_name': 'FlatPage'},
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_flatpages.Categorie']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mot_cle': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'ordre': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        }
    }

    complete_apps = ['custom_flatpages']
