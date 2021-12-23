# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Diffusion'
        db.delete_table('presse_diffusion')

        # Deleting model 'Presse'
        db.delete_table('presse_presse')

        # Adding field 'CommuniquePresse.media'
        db.add_column('presse_communiquepresse', 'media', self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True), keep_default=False)

        # Adding field 'CommuniquePresse.media_photo'
        db.add_column('presse_communiquepresse', 'media_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'CommuniquePresse.lien'
        db.add_column('presse_communiquepresse', 'lien', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'CommuniquePresse.revue_presse'
        db.add_column('presse_communiquepresse', 'revue_presse', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'Diffusion'
        db.create_table('presse_diffusion', (
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('presse', ['Diffusion'])

        # Adding model 'Presse'
        db.create_table('presse_presse', (
            ('lien', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('diffusion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['presse.Diffusion'], null=True, blank=True)),
            ('fichier', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('media', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(max_length=50, unique_with=(), unique=True, populate_from=None, db_index=True)),
            ('extrait', self.gf('django.db.models.fields.TextField')()),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('media_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
        ))
        db.send_create_signal('presse', ['Presse'])

        # Deleting field 'CommuniquePresse.media'
        db.delete_column('presse_communiquepresse', 'media')

        # Deleting field 'CommuniquePresse.media_photo'
        db.delete_column('presse_communiquepresse', 'media_photo')

        # Deleting field 'CommuniquePresse.lien'
        db.delete_column('presse_communiquepresse', 'lien')

        # Deleting field 'CommuniquePresse.revue_presse'
        db.delete_column('presse_communiquepresse', 'revue_presse')


    models = {
        'presse.communiquepresse': {
            'Meta': {'ordering': "['-date']", 'object_name': 'CommuniquePresse'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'fichier': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fichier_ar': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fichier_en': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lien': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'media': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'media_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'revue_presse': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['presse']
