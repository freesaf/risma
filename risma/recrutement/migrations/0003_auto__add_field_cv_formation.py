# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'CV.formation'
        db.add_column('recrutement_cv', 'formation', self.gf('django.db.models.fields.CharField')(default='bac+5', max_length=250), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'CV.formation'
        db.delete_column('recrutement_cv', 'formation')


    models = {
        'recrutement.cv': {
            'Meta': {'object_name': 'CV'},
            'cv': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_naissance': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'formation': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lettre_motivation': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'offre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recrutement.Offre']"}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'recrutement.offre': {
            'Meta': {'object_name': 'Offre'},
            'date_de_cloture': ('django.db.models.fields.DateField', [], {}),
            'division': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intitule_du_poste': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'localisation': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'mission': ('django.db.models.fields.TextField', [], {}),
            'nomposte': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'profil': ('django.db.models.fields.TextField', [], {}),
            'ref': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'secteur_dactivite': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['recrutement']
