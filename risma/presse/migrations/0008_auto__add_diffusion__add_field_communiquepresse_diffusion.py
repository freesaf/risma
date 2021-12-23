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

        # Adding field 'CommuniquePresse.diffusion'
        db.add_column('presse_communiquepresse', 'diffusion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['presse.Diffusion'], null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Diffusion'
        db.delete_table('presse_diffusion')

        # Deleting field 'CommuniquePresse.diffusion'
        db.delete_column('presse_communiquepresse', 'diffusion_id')


    models = {
        'presse.communiquepresse': {
            'Meta': {'ordering': "['-date']", 'object_name': 'CommuniquePresse'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'diffusion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['presse.Diffusion']", 'null': 'True', 'blank': 'True'}),
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
        },
        'presse.diffusion': {
            'Meta': {'object_name': 'Diffusion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['presse']
