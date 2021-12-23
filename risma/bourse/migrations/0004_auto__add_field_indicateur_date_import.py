# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Indicateur.date_import'
        db.add_column('bourse_indicateur', 'date_import', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Indicateur.date_import'
        db.delete_column('bourse_indicateur', 'date_import')


    models = {
        'bourse.cours': {
            'Meta': {'object_name': 'Cours'},
            'capitaux': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'date_import': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dernier': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plus_bas': ('django.db.models.fields.FloatField', [], {}),
            'plus_haut': ('django.db.models.fields.FloatField', [], {}),
            'premier': ('django.db.models.fields.FloatField', [], {}),
            'volume': ('django.db.models.fields.FloatField', [], {})
        },
        'bourse.indicateur': {
            'Meta': {'object_name': 'Indicateur'},
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'curseur': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'date_import': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isin': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'last_quote': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'market_center': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'variation': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['bourse']
