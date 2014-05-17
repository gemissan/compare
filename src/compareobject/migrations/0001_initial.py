# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CompareObjectType'
        db.create_table('compareobject_compareobjecttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal('compareobject', ['CompareObjectType'])

        # Adding M2M table for field features on 'CompareObjectType'
        m2m_table_name = db.shorten_name('compareobject_compareobjecttype_features')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('compareobjecttype', models.ForeignKey(orm['compareobject.compareobjecttype'], null=False)),
            ('comparefeature', models.ForeignKey(orm['comparelist.comparefeature'], null=False))
        ))
        db.create_unique(m2m_table_name, ['compareobjecttype_id', 'comparefeature_id'])

        # Adding model 'CompareCategory'
        db.create_table('compareobject_comparecategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compareuser.CompareUser'], null=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('compareobject', ['CompareCategory'])

        # Adding unique constraint on 'CompareCategory', fields ['name', 'creator']
        db.create_unique('compareobject_comparecategory', ['name', 'creator_id'])

        # Adding model 'CompareObject'
        db.create_table('compareobject_compareobject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='compare_objects', to=orm['compareobject.CompareObjectType'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('compareobject', ['CompareObject'])

        # Adding M2M table for field categories on 'CompareObject'
        m2m_table_name = db.shorten_name('compareobject_compareobject_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('compareobject', models.ForeignKey(orm['compareobject.compareobject'], null=False)),
            ('comparecategory', models.ForeignKey(orm['compareobject.comparecategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['compareobject_id', 'comparecategory_id'])

        # Adding model 'Comparision'
        db.create_table('compareobject_comparision', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comparer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compareuser.CompareUser'])),
            ('compare_list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['comparelist.CompareList'])),
            ('compare_feature', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['comparelist.CompareFeature'], null=True)),
            ('compare_object_better', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comparisions_better', to=orm['compareobject.CompareObject'])),
            ('compare_object_worse', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comparisions_worse', to=orm['compareobject.CompareObject'])),
            ('is_equal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('compareobject', ['Comparision'])

        # Adding unique constraint on 'Comparision', fields ['comparer', 'compare_list', 'compare_feature', 'compare_object_better', 'compare_object_worse']
        db.create_unique('compareobject_comparision', ['comparer_id', 'compare_list_id', 'compare_feature_id', 'compare_object_better_id', 'compare_object_worse_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Comparision', fields ['comparer', 'compare_list', 'compare_feature', 'compare_object_better', 'compare_object_worse']
        db.delete_unique('compareobject_comparision', ['comparer_id', 'compare_list_id', 'compare_feature_id', 'compare_object_better_id', 'compare_object_worse_id'])

        # Removing unique constraint on 'CompareCategory', fields ['name', 'creator']
        db.delete_unique('compareobject_comparecategory', ['name', 'creator_id'])

        # Deleting model 'CompareObjectType'
        db.delete_table('compareobject_compareobjecttype')

        # Removing M2M table for field features on 'CompareObjectType'
        db.delete_table(db.shorten_name('compareobject_compareobjecttype_features'))

        # Deleting model 'CompareCategory'
        db.delete_table('compareobject_comparecategory')

        # Deleting model 'CompareObject'
        db.delete_table('compareobject_compareobject')

        # Removing M2M table for field categories on 'CompareObject'
        db.delete_table(db.shorten_name('compareobject_compareobject_categories'))

        # Deleting model 'Comparision'
        db.delete_table('compareobject_comparision')


    models = {
        'comparelist.comparefeature': {
            'Meta': {'unique_together': "(('name', 'user'),)", 'object_name': 'CompareFeature'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compareuser.CompareUser']", 'null': 'True'})
        },
        'comparelist.comparelist': {
            'Meta': {'unique_together': "(('owner', 'name'),)", 'object_name': 'CompareList'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'compare_lists'", 'symmetrical': 'False', 'to': "orm['compareobject.CompareCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'compare_list'", 'symmetrical': 'False', 'to': "orm['comparelist.CompareFeature']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'list_objects': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'compare_lists'", 'symmetrical': 'False', 'to': "orm['compareobject.CompareObject']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compare_lists'", 'to': "orm['compareobject.CompareObjectType']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owned_lists'", 'to': "orm['compareuser.CompareUser']"})
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
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['comparelist.CompareFeature']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'compareobject.comparision': {
            'Meta': {'unique_together': "(('comparer', 'compare_list', 'compare_feature', 'compare_object_better', 'compare_object_worse'),)", 'object_name': 'Comparision'},
            'compare_feature': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['comparelist.CompareFeature']", 'null': 'True'}),
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
            'allowed_object_types': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['compareobject.CompareObjectType']", 'symmetrical': 'False'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'favourite_lists': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'favourited_users'", 'symmetrical': 'False', 'to': "orm['comparelist.CompareList']"}),
            'favourite_views': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'favourited_users'", 'symmetrical': 'False', 'to': "orm['comparelist.CompareView']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['compareuser.CompareUser']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'repository': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'repository_owner'", 'null': 'True', 'to': "orm['comparelist.CompareList']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['compareobject']