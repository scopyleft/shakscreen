# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CharacterRole'
        db.create_table('filmography_characterrole', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('reference', self.gf('django.db.models.fields.SlugField')(max_length=30, db_index=True)),
        ))
        db.send_create_signal('filmography', ['CharacterRole'])

        # Adding model 'Character'
        db.create_table('filmography_character', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
        ))
        db.send_create_signal('filmography', ['Character'])

        # Adding M2M table for field roles on 'Character'
        db.create_table('filmography_character_roles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('character', models.ForeignKey(orm['filmography.character'], null=False)),
            ('characterrole', models.ForeignKey(orm['filmography.characterrole'], null=False))
        ))
        db.create_unique('filmography_character_roles', ['character_id', 'characterrole_id'])


    def backwards(self, orm):
        
        # Deleting model 'CharacterRole'
        db.delete_table('filmography_characterrole')

        # Deleting model 'Character'
        db.delete_table('filmography_character')

        # Removing M2M table for field roles on 'Character'
        db.delete_table('filmography_character_roles')


    models = {
        'filmography.character': {
            'Meta': {'object_name': 'Character'},
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['filmography.CharacterRole']", 'symmetrical': 'False'})
        },
        'filmography.characterrole': {
            'Meta': {'object_name': 'CharacterRole'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'reference': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'db_index': 'True'})
        },
        'filmography.contributor': {
            'Meta': {'object_name': 'Contributor'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '1', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['filmography']
