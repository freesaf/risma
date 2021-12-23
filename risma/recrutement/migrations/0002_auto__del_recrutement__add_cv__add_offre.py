# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Recrutement'
        db.delete_table('recrutement_recrutement')

        # Adding model 'CV'
        db.create_table('recrutement_cv', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('date_naissance', self.gf('django.db.models.fields.DateField')()),
            ('ville', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('cv', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('lettre_motivation', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('offre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recrutement.Offre'])),
        ))
        db.send_create_signal('recrutement', ['CV'])

        # Adding model 'Offre'
        db.create_table('recrutement_offre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nomposte', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('ref', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_de_cloture', self.gf('django.db.models.fields.DateField')()),
            ('intitule_du_poste', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('mission', self.gf('django.db.models.fields.TextField')()),
            ('profil', self.gf('django.db.models.fields.TextField')()),
            ('division', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('secteur_dactivite', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('localisation', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('recrutement', ['Offre'])


    def backwards(self, orm):
        
        # Adding model 'Recrutement'
        db.create_table('recrutement_recrutement', (
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('ville', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('date_naissance', self.gf('django.db.models.fields.DateField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('lettre_motivation', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('cv', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('recrutement', ['Recrutement'])

        # Deleting model 'CV'
        db.delete_table('recrutement_cv')

        # Deleting model 'Offre'
        db.delete_table('recrutement_offre')


    models = {
        'recrutement.cv': {
            'Meta': {'object_name': 'CV'},
            'cv': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_naissance': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
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
