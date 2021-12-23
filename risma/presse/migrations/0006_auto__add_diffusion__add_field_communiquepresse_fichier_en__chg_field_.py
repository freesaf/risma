# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Diffusion'
        db.create_table('presse_diffusion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('presse', ['Diffusion'])

        # Adding field 'CommuniquePresse.fichier_en'
        db.add_column('presse_communiquepresse', 'fichier_en', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True), keep_default=False)

        # Renaming column for 'Presse.diffusion' to match new field type.
        db.rename_column('presse_presse', 'diffusion', 'diffusion_id')
        # Changing field 'Presse.diffusion'
        db.alter_column('presse_presse', 'diffusion_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['presse.Diffusion'], null=True))

        # Adding index on 'Presse', fields ['diffusion']
        db.create_index('presse_presse', ['diffusion_id'])


    def backwards(self, orm):
        
        # Removing index on 'Presse', fields ['diffusion']
        db.delete_index('presse_presse', ['diffusion_id'])

        # Deleting model 'Diffusion'
        db.delete_table('presse_diffusion')

        # Deleting field 'CommuniquePresse.fichier_en'
        db.delete_column('presse_communiquepresse', 'fichier_en')

        # Renaming column for 'Presse.diffusion' to match new field type.
        db.rename_column('presse_presse', 'diffusion_id', 'diffusion')
        # Changing field 'Presse.diffusion'
        db.alter_column('presse_presse', 'diffusion', self.gf('django.db.models.fields.IntegerField')(null=True))


    models = {
        'presse.communiquepresse': {
            'Meta': {'ordering': "['-date']", 'object_name': 'CommuniquePresse'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'fichier': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fichier_ar': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fichier_en': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'presse.diffusion': {
            'Meta': {'object_name': 'Diffusion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'presse.presse': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Presse'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'diffusion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['presse.Diffusion']", 'null': 'True', 'blank': 'True'}),
            'extrait': ('django.db.models.fields.TextField', [], {}),
            'fichier': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lien': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'media': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'media_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['presse']
