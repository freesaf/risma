# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Cours'
        db.delete_table('bourse_cours')

        # Deleting model 'Indicateur'
        db.delete_table('bourse_indicateur')

        # Adding model 'Cour'
        db.create_table('bourse_cour', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('dernier', self.gf('django.db.models.fields.FloatField')()),
            ('premier', self.gf('django.db.models.fields.FloatField')()),
            ('plus_haut', self.gf('django.db.models.fields.FloatField')()),
            ('plus_bas', self.gf('django.db.models.fields.FloatField')()),
            ('volume', self.gf('django.db.models.fields.FloatField')()),
            ('capitaux', self.gf('django.db.models.fields.FloatField')()),
            ('date_import', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
        ))
        db.send_create_signal('bourse', ['Cour'])


    def backwards(self, orm):
        
        # Adding model 'Cours'
        db.create_table('bourse_cours', (
            ('dernier', self.gf('django.db.models.fields.FloatField')()),
            ('plus_haut', self.gf('django.db.models.fields.FloatField')()),
            ('date_import', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('volume', self.gf('django.db.models.fields.FloatField')()),
            ('capitaux', self.gf('django.db.models.fields.FloatField')()),
            ('premier', self.gf('django.db.models.fields.FloatField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plus_bas', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('bourse', ['Cours'])

        # Adding model 'Indicateur'
        db.create_table('bourse_indicateur', (
            ('curseur', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('market_center', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('isin', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('variation', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('last_quote', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal('bourse', ['Indicateur'])

        # Deleting model 'Cour'
        db.delete_table('bourse_cour')


    models = {
        'bourse.cour': {
            'Meta': {'object_name': 'Cour'},
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
        'bourse.indicator': {
            'Meta': {'object_name': 'Indicator'},
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'curseur': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isin': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'last_quote': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'market_center': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'variation': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['bourse']
