# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Indicator'
        db.create_table('bourse_indicator', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_quote', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('variation', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('curseur', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('isin', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('market_center', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('bourse', ['Indicator'])

        # Changing field 'Indicateur.curseur'
        db.alter_column('bourse_indicateur', 'curseur', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Indicateur.name'
        db.alter_column('bourse_indicateur', 'name', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Indicateur.currency'
        db.alter_column('bourse_indicateur', 'currency', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Indicateur.variation'
        db.alter_column('bourse_indicateur', 'variation', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Indicateur.last_quote'
        db.alter_column('bourse_indicateur', 'last_quote', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Indicateur.market_center'
        db.alter_column('bourse_indicateur', 'market_center', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Indicateur.date'
        db.alter_column('bourse_indicateur', 'date', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Indicateur.isin'
        db.alter_column('bourse_indicateur', 'isin', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))


    def backwards(self, orm):
        
        # Deleting model 'Indicator'
        db.delete_table('bourse_indicator')

        # Changing field 'Indicateur.curseur'
        db.alter_column('bourse_indicateur', 'curseur', self.gf('django.db.models.fields.CharField')(default='', max_length=250))

        # Changing field 'Indicateur.name'
        db.alter_column('bourse_indicateur', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=250))

        # Changing field 'Indicateur.currency'
        db.alter_column('bourse_indicateur', 'currency', self.gf('django.db.models.fields.CharField')(default='', max_length=250))

        # Changing field 'Indicateur.variation'
        db.alter_column('bourse_indicateur', 'variation', self.gf('django.db.models.fields.CharField')(default='', max_length=250))

        # Changing field 'Indicateur.last_quote'
        db.alter_column('bourse_indicateur', 'last_quote', self.gf('django.db.models.fields.CharField')(default='', max_length=250))

        # Changing field 'Indicateur.market_center'
        db.alter_column('bourse_indicateur', 'market_center', self.gf('django.db.models.fields.CharField')(default='', max_length=250))

        # Changing field 'Indicateur.date'
        db.alter_column('bourse_indicateur', 'date', self.gf('django.db.models.fields.CharField')(default='', max_length=250))

        # Changing field 'Indicateur.isin'
        db.alter_column('bourse_indicateur', 'isin', self.gf('django.db.models.fields.CharField')(default='', max_length=250))


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
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'curseur': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isin': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'last_quote': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'market_center': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'variation': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
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
