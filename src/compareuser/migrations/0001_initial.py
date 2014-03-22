# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CompareUser'
        db.create_table(u'compareuser_compareuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('email', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('repository', self.gf('django.db.models.fields.related.ForeignKey')(related_name='repository_owner', null=True, to=orm['comparelist.CompareList'])),
        ))
        db.send_create_signal(u'compareuser', ['CompareUser'])

        # Adding M2M table for field friends on 'CompareUser'
        m2m_table_name = db.shorten_name(u'compareuser_compareuser_friends')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_compareuser', models.ForeignKey(orm[u'compareuser.compareuser'], null=False)),
            ('to_compareuser', models.ForeignKey(orm[u'compareuser.compareuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_compareuser_id', 'to_compareuser_id'])

        # Adding M2M table for field favourite_lists on 'CompareUser'
        m2m_table_name = db.shorten_name(u'compareuser_compareuser_favourite_lists')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('compareuser', models.ForeignKey(orm[u'compareuser.compareuser'], null=False)),
            ('comparelist', models.ForeignKey(orm[u'comparelist.comparelist'], null=False))
        ))
        db.create_unique(m2m_table_name, ['compareuser_id', 'comparelist_id'])

        # Adding M2M table for field favourite_views on 'CompareUser'
        m2m_table_name = db.shorten_name(u'compareuser_compareuser_favourite_views')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('compareuser', models.ForeignKey(orm[u'compareuser.compareuser'], null=False)),
            ('compareview', models.ForeignKey(orm[u'comparelist.compareview'], null=False))
        ))
        db.create_unique(m2m_table_name, ['compareuser_id', 'compareview_id'])

        # Adding M2M table for field allowed_object_types on 'CompareUser'
        m2m_table_name = db.shorten_name(u'compareuser_compareuser_allowed_object_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('compareuser', models.ForeignKey(orm[u'compareuser.compareuser'], null=False)),
            ('compareobjecttype', models.ForeignKey(orm[u'compareobject.compareobjecttype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['compareuser_id', 'compareobjecttype_id'])


    def backwards(self, orm):
        # Deleting model 'CompareUser'
        db.delete_table(u'compareuser_compareuser')

        # Removing M2M table for field friends on 'CompareUser'
        db.delete_table(db.shorten_name(u'compareuser_compareuser_friends'))

        # Removing M2M table for field favourite_lists on 'CompareUser'
        db.delete_table(db.shorten_name(u'compareuser_compareuser_favourite_lists'))

        # Removing M2M table for field favourite_views on 'CompareUser'
        db.delete_table(db.shorten_name(u'compareuser_compareuser_favourite_views'))

        # Removing M2M table for field allowed_object_types on 'CompareUser'
        db.delete_table(db.shorten_name(u'compareuser_compareuser_allowed_object_types'))


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

    complete_apps = ['compareuser']