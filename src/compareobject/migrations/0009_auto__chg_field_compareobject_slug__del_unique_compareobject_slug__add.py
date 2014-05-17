# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'CompareObject', fields ['slug']
        db.delete_unique('compareobject_compareobject', ['slug'])


        # Changing field 'CompareObject.slug'
        db.alter_column('compareobject_compareobject', 'slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='name'))
        # Adding field 'CompareCategory.slug'
        db.add_column('compareobject_comparecategory', 'slug',
                      self.gf('autoslug.fields.AutoSlugField')(default=None, unique_with=(), max_length=50, populate_from='name'),
                      keep_default=False)

        # Adding field 'CompareObjectType.slug'
        db.add_column('compareobject_compareobjecttype', 'slug',
                      self.gf('autoslug.fields.AutoSlugField')(default=None, unique_with=(), max_length=50, populate_from='name'),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'CompareObject.slug'
        db.alter_column('compareobject_compareobject', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=255, unique=True))
        # Adding unique constraint on 'CompareObject', fields ['slug']
        db.create_unique('compareobject_compareobject', ['slug'])

        # Deleting field 'CompareCategory.slug'
        db.delete_column('compareobject_comparecategory', 'slug')

        # Deleting field 'CompareObjectType.slug'
        db.delete_column('compareobject_compareobjecttype', 'slug')


    models = {
        'comparelist.comparefeature': {
            'Meta': {'unique_together': "(('user', 'name'),)", 'object_name': 'CompareFeature'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compareuser.CompareUser']", 'null': 'True', 'blank': 'True'})
        },
        'comparelist.comparelist': {
            'Meta': {'unique_together': "[['owner', 'repository_owner', 'name']]", 'object_name': 'CompareList', 'index_together': "[['owner', 'object_type'], ['owner', 'private'], ['repository_owner', 'object_type']]"},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'compare_lists'", 'blank': 'True', 'to': "orm['compareobject.CompareCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'compare_list'", 'blank': 'True', 'to': "orm['comparelist.CompareFeature']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_objects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'compare_lists'", 'blank': 'True', 'to': "orm['compareobject.CompareObject']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compare_lists'", 'blank': 'True', 'to': "orm['compareobject.CompareObjectType']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'owned_lists'", 'null': 'True', 'blank': 'True', 'to': "orm['compareuser.CompareUser']"}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'repository_owner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'repositories'", 'null': 'True', 'blank': 'True', 'to': "orm['compareuser.CompareUser']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None'})
        },
        'comparelist.compareview': {
            'Meta': {'object_name': 'CompareView'},
            'compare_list': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compare_views'", 'to': "orm['comparelist.CompareList']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'excluded_categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'excluded_views'", 'symmetrical': 'False', 'to': "orm['compareobject.CompareCategory']"}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'compare_views'", 'symmetrical': 'False', 'to': "orm['comparelist.CompareFeature']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'included_categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'included_views'", 'symmetrical': 'False', 'to': "orm['compareobject.CompareCategory']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owned_views'", 'to': "orm['compareuser.CompareUser']"}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'compareobject.comparecategory': {
            'Meta': {'unique_together': "(('name', 'creator'),)", 'object_name': 'CompareCategory'},
            'category_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['compareuser.CompareUser']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"})
        },
        'compareobject.compareobject': {
            'Meta': {'object_name': 'CompareObject'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'compare_objects'", 'blank': 'True', 'to': "orm['compareobject.CompareCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compare_objects'", 'to': "orm['compareobject.CompareObjectType']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"})
        },
        'compareobject.compareobjecttype': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'CompareObjectType'},
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['comparelist.CompareFeature']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_view': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'list_view': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'ordering': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"})
        },
        'compareobject.comparision': {
            'Meta': {'unique_together': "(('comparer', 'compare_list', 'compare_feature', 'compare_object_better', 'compare_object_worse'),)", 'object_name': 'Comparision'},
            'compare_feature': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['comparelist.CompareFeature']", 'null': 'True', 'blank': 'True'}),
            'compare_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['comparelist.CompareList']"}),
            'compare_object_better': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comparisions_better'", 'to': "orm['compareobject.CompareObject']"}),
            'compare_object_worse': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comparisions_worse'", 'to': "orm['compareobject.CompareObject']"}),
            'comparer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compareuser.CompareUser']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_equal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        'compareuser.compareuser': {
            'Meta': {'object_name': 'CompareUser'},
            'allowed_object_types': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['compareobject.CompareObjectType']", 'symmetrical': 'False', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'favourite_lists': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'favourited_users'", 'blank': 'True', 'to': "orm['comparelist.CompareList']"}),
            'favourite_views': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'favourited_users'", 'blank': 'True', 'to': "orm['comparelist.CompareView']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['compareuser.CompareUser']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'username'"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['compareobject']