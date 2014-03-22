# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CompareFeature'
        db.create_table(u'comparelist_comparefeature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['compareuser.CompareUser'], null=True)),
        ))
        db.send_create_signal(u'comparelist', ['CompareFeature'])

        # Adding unique constraint on 'CompareFeature', fields ['name', 'user']
        db.create_unique(u'comparelist_comparefeature', ['name', 'user_id'])

        # Adding model 'CompareList'
        db.create_table(u'comparelist_comparelist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='owned_lists', to=orm['compareuser.CompareUser'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('object_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='compare_lists', to=orm['compareobject.CompareObjectType'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('is_private', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'comparelist', ['CompareList'])

        # Adding unique constraint on 'CompareList', fields ['owner', 'name']
        db.create_unique(u'comparelist_comparelist', ['owner_id', 'name'])

        # Adding M2M table for field categories on 'CompareList'
        m2m_table_name = db.shorten_name(u'comparelist_comparelist_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comparelist', models.ForeignKey(orm[u'comparelist.comparelist'], null=False)),
            ('comparecategory', models.ForeignKey(orm[u'compareobject.comparecategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['comparelist_id', 'comparecategory_id'])

        # Adding M2M table for field features on 'CompareList'
        m2m_table_name = db.shorten_name(u'comparelist_comparelist_features')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comparelist', models.ForeignKey(orm[u'comparelist.comparelist'], null=False)),
            ('comparefeature', models.ForeignKey(orm[u'comparelist.comparefeature'], null=False))
        ))
        db.create_unique(m2m_table_name, ['comparelist_id', 'comparefeature_id'])

        # Adding M2M table for field list_objects on 'CompareList'
        m2m_table_name = db.shorten_name(u'comparelist_comparelist_list_objects')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comparelist', models.ForeignKey(orm[u'comparelist.comparelist'], null=False)),
            ('compareobject', models.ForeignKey(orm[u'compareobject.compareobject'], null=False))
        ))
        db.create_unique(m2m_table_name, ['comparelist_id', 'compareobject_id'])

        # Adding model 'CompareView'
        db.create_table(u'comparelist_compareview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='owned_views', to=orm['compareuser.CompareUser'])),
            ('compare_list', self.gf('django.db.models.fields.related.ForeignKey')(related_name='compare_views', to=orm['comparelist.CompareList'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('is_private', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'comparelist', ['CompareView'])

        # Adding M2M table for field included_categories on 'CompareView'
        m2m_table_name = db.shorten_name(u'comparelist_compareview_included_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('compareview', models.ForeignKey(orm[u'comparelist.compareview'], null=False)),
            ('comparecategory', models.ForeignKey(orm[u'compareobject.comparecategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['compareview_id', 'comparecategory_id'])

        # Adding M2M table for field excluded_categories on 'CompareView'
        m2m_table_name = db.shorten_name(u'comparelist_compareview_excluded_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('compareview', models.ForeignKey(orm[u'comparelist.compareview'], null=False)),
            ('comparecategory', models.ForeignKey(orm[u'compareobject.comparecategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['compareview_id', 'comparecategory_id'])

        # Adding M2M table for field features on 'CompareView'
        m2m_table_name = db.shorten_name(u'comparelist_compareview_features')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('compareview', models.ForeignKey(orm[u'comparelist.compareview'], null=False)),
            ('comparefeature', models.ForeignKey(orm[u'comparelist.comparefeature'], null=False))
        ))
        db.create_unique(m2m_table_name, ['compareview_id', 'comparefeature_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'CompareList', fields ['owner', 'name']
        db.delete_unique(u'comparelist_comparelist', ['owner_id', 'name'])

        # Removing unique constraint on 'CompareFeature', fields ['name', 'user']
        db.delete_unique(u'comparelist_comparefeature', ['name', 'user_id'])

        # Deleting model 'CompareFeature'
        db.delete_table(u'comparelist_comparefeature')

        # Deleting model 'CompareList'
        db.delete_table(u'comparelist_comparelist')

        # Removing M2M table for field categories on 'CompareList'
        db.delete_table(db.shorten_name(u'comparelist_comparelist_categories'))

        # Removing M2M table for field features on 'CompareList'
        db.delete_table(db.shorten_name(u'comparelist_comparelist_features'))

        # Removing M2M table for field list_objects on 'CompareList'
        db.delete_table(db.shorten_name(u'comparelist_comparelist_list_objects'))

        # Deleting model 'CompareView'
        db.delete_table(u'comparelist_compareview')

        # Removing M2M table for field included_categories on 'CompareView'
        db.delete_table(db.shorten_name(u'comparelist_compareview_included_categories'))

        # Removing M2M table for field excluded_categories on 'CompareView'
        db.delete_table(db.shorten_name(u'comparelist_compareview_excluded_categories'))

        # Removing M2M table for field features on 'CompareView'
        db.delete_table(db.shorten_name(u'comparelist_compareview_features'))


    models = {
        u'comparelist.comparefeature': {
            'Meta': {'unique_together': "(('name', 'user'),)", 'object_name': 'CompareFeature'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compareuser.CompareUser']", 'null': 'True'})
        },
        u'comparelist.comparelist': {
            'Meta': {'unique_together': "(('owner', 'name'),)", 'object_name': 'CompareList'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'compare_lists'", 'symmetrical': 'False', 'to': u"orm['compareobject.CompareCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'compare_list'", 'symmetrical': 'False', 'to': u"orm['comparelist.CompareFeature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'list_objects': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'compare_lists'", 'symmetrical': 'False', 'to': u"orm['compareobject.CompareObject']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compare_lists'", 'to': u"orm['compareobject.CompareObjectType']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owned_lists'", 'to': u"orm['compareuser.CompareUser']"})
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
            'Meta': {'object_name': 'CompareObjectType'},
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['comparelist.CompareFeature']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'compareuser.compareuser': {
            'Meta': {'object_name': 'CompareUser'},
            'allowed_object_types': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['compareobject.CompareObjectType']", 'symmetrical': 'False'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'favourite_lists': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'favourited_users'", 'symmetrical': 'False', 'to': u"orm['comparelist.CompareList']"}),
            'favourite_views': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'favourited_users'", 'symmetrical': 'False', 'to': u"orm['comparelist.CompareView']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['compareuser.CompareUser']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'repository': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'repository_owner'", 'null': 'True', 'to': u"orm['comparelist.CompareList']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['comparelist']