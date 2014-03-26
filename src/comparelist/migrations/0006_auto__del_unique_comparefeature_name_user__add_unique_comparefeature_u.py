# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'CompareFeature', fields ['name', 'user']
        db.delete_unique(u'comparelist_comparefeature', ['name', 'user_id'])

        # Adding unique constraint on 'CompareFeature', fields ['user', 'name']
        db.create_unique(u'comparelist_comparefeature', ['user_id', 'name'])


        # Changing field 'CompareList.object_type'
        db.alter_column(u'comparelist_comparelist', 'object_type_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['compareobject.CompareObjectType']))
        # Deleting field 'CompareView.is_private'
        db.delete_column(u'comparelist_compareview', 'is_private')

        # Adding field 'CompareView.private'
        db.add_column(u'comparelist_compareview', 'private',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'CompareFeature', fields ['user', 'name']
        db.delete_unique(u'comparelist_comparefeature', ['user_id', 'name'])

        # Adding unique constraint on 'CompareFeature', fields ['name', 'user']
        db.create_unique(u'comparelist_comparefeature', ['name', 'user_id'])


        # Changing field 'CompareList.object_type'
        db.alter_column(u'comparelist_comparelist', 'object_type_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['compareobject.CompareObjectType']))
        # Adding field 'CompareView.is_private'
        db.add_column(u'comparelist_compareview', 'is_private',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Deleting field 'CompareView.private'
        db.delete_column(u'comparelist_compareview', 'private')


    models = {
        u'comparelist.comparefeature': {
            'Meta': {'unique_together': "(('user', 'name'),)", 'object_name': 'CompareFeature'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compareuser.CompareUser']", 'null': 'True'})
        },
        u'comparelist.comparelist': {
            'Meta': {'unique_together': "[['owner', 'repository_owner', 'name']]", 'object_name': 'CompareList', 'index_together': "[['owner', 'object_type'], ['owner', 'private'], ['repository_owner', 'object_type']]"},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'compare_lists'", 'blank': 'True', 'to': u"orm['compareobject.CompareCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'compare_list'", 'blank': 'True', 'to': u"orm['comparelist.CompareFeature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_objects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'compare_lists'", 'blank': 'True', 'to': u"orm['compareobject.CompareObject']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compare_lists'", 'blank': 'True', 'to': u"orm['compareobject.CompareObjectType']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'owned_lists'", 'null': 'True', 'blank': 'True', 'to': u"orm['compareuser.CompareUser']"}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'repository_owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'repositories'", 'null': 'True', 'blank': 'True', 'to': u"orm['compareuser.CompareUser']"})
        },
        u'comparelist.compareview': {
            'Meta': {'object_name': 'CompareView'},
            'compare_list': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compare_views'", 'to': u"orm['comparelist.CompareList']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluded_categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'excluded_views'", 'symmetrical': 'False', 'to': u"orm['compareobject.CompareCategory']"}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'compare_views'", 'symmetrical': 'False', 'to': u"orm['comparelist.CompareFeature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'included_categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'included_views'", 'symmetrical': 'False', 'to': u"orm['compareobject.CompareCategory']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owned_views'", 'to': u"orm['compareuser.CompareUser']"}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'compareobject.comparecategory': {
            'Meta': {'unique_together': "(('name', 'creator'),)", 'object_name': 'CompareCategory'},
            'category_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['compareuser.CompareUser']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'compareobject.compareobject': {
            'Meta': {'object_name': 'CompareObject'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'compare_objects'", 'blank': 'True', 'to': u"orm['compareobject.CompareCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compare_objects'", 'to': u"orm['compareobject.CompareObjectType']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'compareobject.compareobjecttype': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'CompareObjectType'},
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['comparelist.CompareFeature']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_view': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'list_view': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'ordering': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        u'compareuser.compareuser': {
            'Meta': {'object_name': 'CompareUser'},
            'allowed_object_types': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['compareobject.CompareObjectType']", 'symmetrical': 'False', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'favourite_lists': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'favourited_users'", 'blank': 'True', 'to': u"orm['comparelist.CompareList']"}),
            'favourite_views': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'favourited_users'", 'blank': 'True', 'to': u"orm['comparelist.CompareView']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['compareuser.CompareUser']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['comparelist']