# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CompareList.object_type'
        db.alter_column('comparelist_comparelist', 'object_type_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['compareobject.CompareObjectType']))

        # Changing field 'CompareList.owner'
        db.alter_column('comparelist_comparelist', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['compareuser.CompareUser']))

    def backwards(self, orm):

        # Changing field 'CompareList.object_type'
        db.alter_column('comparelist_comparelist', 'object_type_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['compareobject.CompareObjectType']))

        # Changing field 'CompareList.owner'
        db.alter_column('comparelist_comparelist', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['compareuser.CompareUser']))

    models = {
        'comparelist.comparefeature': {
            'Meta': {'unique_together': "(('name', 'user'),)", 'object_name': 'CompareFeature'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compareuser.CompareUser']", 'null': 'True'})
        },
        'comparelist.comparelist': {
            'Meta': {'unique_together': "(('owner', 'name'),)", 'object_name': 'CompareList'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'related_name': "'compare_lists'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['compareobject.CompareCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'related_name': "'compare_list'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['comparelist.CompareFeature']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'list_objects': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'related_name': "'compare_lists'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['compareobject.CompareObject']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_type': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'compare_lists'", 'null': 'True', 'to': "orm['compareobject.CompareObjectType']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owned_lists'", 'null': 'True', 'to': "orm['compareuser.CompareUser']"})
        },
        'comparelist.compareview': {
            'Meta': {'object_name': 'CompareView'},
            'compare_list': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compare_views'", 'to': "orm['comparelist.CompareList']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluded_categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'excluded_views'", 'symmetrical': 'False', 'to': "orm['compareobject.CompareCategory']"}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'compare_views'", 'symmetrical': 'False', 'to': "orm['comparelist.CompareFeature']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'included_categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'included_views'", 'symmetrical': 'False', 'to': "orm['compareobject.CompareCategory']"}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owned_views'", 'to': "orm['compareuser.CompareUser']"})
        },
        'compareobject.comparecategory': {
            'Meta': {'unique_together': "(('name', 'creator'),)", 'object_name': 'CompareCategory'},
            'category_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compareuser.CompareUser']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'compareobject.compareobject': {
            'Meta': {'object_name': 'CompareObject'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'compare_objects'", 'symmetrical': 'False', 'to': "orm['compareobject.CompareCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compare_objects'", 'to': "orm['compareobject.CompareObjectType']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        },
        'compareobject.compareobjecttype': {
            'Meta': {'object_name': 'CompareObjectType'},
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['comparelist.CompareFeature']", 'null': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'compareuser.compareuser': {
            'Meta': {'object_name': 'CompareUser'},
            'allowed_object_types': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['compareobject.CompareObjectType']", 'symmetrical': 'False'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'favourite_lists': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'favourited_users'", 'null': 'True', 'to': "orm['comparelist.CompareList']"}),
            'favourite_views': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'favourited_users'", 'null': 'True', 'to': "orm['comparelist.CompareView']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['compareuser.CompareUser']", 'null': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'repository': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'repository_owner'", 'to': "orm['comparelist.CompareList']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['comparelist']