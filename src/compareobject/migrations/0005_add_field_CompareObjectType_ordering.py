# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CompareObjectType.ordering'
        db.add_column(u'compareobject_compareobjecttype', 'ordering',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CompareObjectType.ordering'
        db.delete_column(u'compareobject_compareobjecttype', 'ordering')


    models = {
        u'comparelist.comparefeature': {
            'Meta': {'unique_together': "(('name', 'user'),)", 'object_name': 'CompareFeature'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compareuser.CompareUser']", 'null': 'True'})
        },
        u'comparelist.comparelist': {
            'Meta': {'unique_together': "[['owner', 'repository_owner', 'name']]", 'object_name': 'CompareList', 'index_together': "[['owner', 'object_type'], ['owner', 'private'], ['repository_owner', 'object_type']]"},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'related_name': "'compare_lists'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['compareobject.CompareCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'related_name': "'compare_list'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['comparelist.CompareFeature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_objects': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'related_name': "'compare_lists'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['compareobject.CompareObject']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_type': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'compare_lists'", 'null': 'True', 'to': u"orm['compareobject.CompareObjectType']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'owned_lists'", 'null': 'True', 'to': u"orm['compareuser.CompareUser']"}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'repository_owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'repositories'", 'null': 'True', 'to': u"orm['compareuser.CompareUser']"})
        },
        u'comparelist.compareview': {
            'Meta': {'object_name': 'CompareView'},
            'compare_list': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compare_views'", 'to': u"orm['comparelist.CompareList']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluded_categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'excluded_views'", 'symmetrical': 'False', 'to': u"orm['compareobject.CompareCategory']"}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'compare_views'", 'symmetrical': 'False', 'to': u"orm['comparelist.CompareFeature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'included_categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'included_views'", 'symmetrical': 'False', 'to': u"orm['compareobject.CompareCategory']"}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owned_views'", 'to': u"orm['compareuser.CompareUser']"})
        },
        u'compareobject.comparecategory': {
            'Meta': {'unique_together': "(('name', 'creator'),)", 'object_name': 'CompareCategory'},
            'category_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compareuser.CompareUser']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'compareobject.compareobject': {
            'Meta': {'object_name': 'CompareObject'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'compare_objects'", 'symmetrical': 'False', 'to': u"orm['compareobject.CompareCategory']"}),
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
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['comparelist.CompareFeature']", 'null': 'True', 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'ordering': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'compareobject.comparision': {
            'Meta': {'unique_together': "(('comparer', 'compare_list', 'compare_feature', 'compare_object_better', 'compare_object_worse'),)", 'object_name': 'Comparision'},
            'compare_feature': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['comparelist.CompareFeature']", 'null': 'True'}),
            'compare_list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['comparelist.CompareList']"}),
            'compare_object_better': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comparisions_better'", 'to': u"orm['compareobject.CompareObject']"}),
            'compare_object_worse': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comparisions_worse'", 'to': u"orm['compareobject.CompareObject']"}),
            'comparer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compareuser.CompareUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_equal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'compareuser.compareuser': {
            'Meta': {'object_name': 'CompareUser'},
            'allowed_object_types': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['compareobject.CompareObjectType']", 'symmetrical': 'False'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'favourite_lists': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'favourited_users'", 'null': 'True', 'to': u"orm['comparelist.CompareList']"}),
            'favourite_views': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'favourited_users'", 'null': 'True', 'to': u"orm['comparelist.CompareView']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['compareuser.CompareUser']", 'null': 'True', 'symmetrical': 'False'}),
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

    complete_apps = ['compareobject']