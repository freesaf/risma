# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Categorie'
        db.create_table('custom_flatpages_categorie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('custom_flatpages', ['Categorie'])

        # Adding model 'FlatPage'
        db.create_table('custom_flatpages_flatpage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('categorie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['custom_flatpages.Categorie'], null=True, blank=True)),
            ('mot_cle', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('enable_comments', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('template_name', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('registration_required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ordre', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('custom_flatpages', ['FlatPage'])

        # Adding model 'Contenu'
        db.create_table('custom_flatpages_contenu', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('flatpage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['custom_flatpages.FlatPage'])),
        ))
        db.send_create_signal('custom_flatpages', ['Contenu'])


    def backwards(self, orm):
        
        # Deleting model 'Categorie'
        db.delete_table('custom_flatpages_categorie')

        # Deleting model 'FlatPage'
        db.delete_table('custom_flatpages_flatpage')

        # Deleting model 'Contenu'
        db.delete_table('custom_flatpages_contenu')


    models = {
        'custom_flatpages.categorie': {
            'Meta': {'object_name': 'Categorie'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'custom_flatpages.contenu': {
            'Meta': {'object_name': 'Contenu'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'flatpage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_flatpages.FlatPage']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'custom_flatpages.flatpage': {
            'Meta': {'ordering': "('url',)", 'object_name': 'FlatPage'},
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['custom_flatpages.Categorie']", 'null': 'True', 'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mot_cle': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'ordre': ('django.db.models.fields.IntegerField', [], {}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        }
    }

    complete_apps = ['custom_flatpages']
