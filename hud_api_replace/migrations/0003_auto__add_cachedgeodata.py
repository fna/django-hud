# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CachedGeodata'
        db.create_table(u'hud_api_replace_cachedgeodata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('lon', self.gf('django.db.models.fields.FloatField')()),
            ('expires', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
        ))
        db.send_create_signal(u'hud_api_replace', ['CachedGeodata'])


    def backwards(self, orm):
        # Deleting model 'CachedGeodata'
        db.delete_table(u'hud_api_replace_cachedgeodata')


    models = {
        u'hud_api_replace.cachedgeodata': {
            'Meta': {'object_name': 'CachedGeodata'},
            'expires': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lon': ('django.db.models.fields.FloatField', [], {})
        },
        u'hud_api_replace.counselingagency': {
            'Meta': {'object_name': 'CounselingAgency'},
            'adr1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'adr2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'agc_ADDR_LATITUDE': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'agc_ADDR_LONGITUDE': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'agc_SRC_CD': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'agc_STATUS': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'agcid': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'colonias_IND': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'counslg_METHOD': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'county_nme': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'faithbased': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'languages': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mailingadr1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mailingadr2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mailingcity': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mailingstatecd': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'mailingzipcd': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'migrantwkrs_IND': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nme': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parentid': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'phone1': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'phone2': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'services': ('django.db.models.fields.CharField', [], {'max_length': '1500'}),
            'state_FIPS_CODE': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state_NME': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'statecd': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'weburl': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zipcd': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'hud_api_replace.language': {
            'Meta': {'object_name': 'Language'},
            'abbr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'hud_api_replace.service': {
            'Meta': {'object_name': 'Service'},
            'abbr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['hud_api_replace']