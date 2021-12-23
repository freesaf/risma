# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Categorie'
        db.create_table('popup_categorie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('popup', ['Categorie'])

        # Adding model 'Popup'
        db.create_table('popup_popup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('texte', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('lien', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('date_debut', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_fin', self.gf('django.db.models.fields.DateTimeField')()),
            ('categorie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['popup.Categorie'])),
        ))
        db.send_create_signal('popup', ['Popup'])


    def backwards(self, orm):
        
        # Deleting model 'Categorie'
        db.delete_table('popup_categorie')

        # Deleting model 'Popup'
        db.delete_table('popup_popup')


    models = {
        'popup.categorie': {
            'Meta': {'object_name': 'Categorie'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'popup.popup': {
            'Meta': {'object_name': 'Popup'},
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['popup.Categorie']"}),
            'date_debut': ('django.db.models.fields.DateTimeField', [], {}),
            'date_fin': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lien': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'texte': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['popup']
