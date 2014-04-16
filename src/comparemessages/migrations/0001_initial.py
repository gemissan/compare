# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Message'
        db.create_table(u'comparemessages_message', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'comparemessages', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table(u'comparemessages_message')


    models = {
        u'comparemessages.message': {
            'Meta': {'ordering': "['name']", 'object_name': 'Message'},
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'})
        }
    }

    complete_apps = ['comparemessages']