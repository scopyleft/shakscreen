# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Analysis.description'
        db.delete_column('filmography_analysis', 'description')

        # Adding field 'Analysis.summary'
        db.add_column('filmography_analysis', 'summary', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Analysis.description'
        db.add_column('filmography_analysis', 'description', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Deleting field 'Analysis.summary'
        db.delete_column('filmography_analysis', 'summary')


    models = {
        'filmography.analysis': {
            'Meta': {'object_name': 'Analysis'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'contributors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['filmography.Contributor']", 'symmetrical': 'False'}),
            'films': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['filmography.Film']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        },
        'filmography.film': {
            'Meta': {'object_name': 'Film'},
            'actors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'actor_films'", 'symmetrical': 'False', 'through': "orm['filmography.FilmCharacter']", 'to': "orm['filmography.Character']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'cinematographers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'cinematographer_films'", 'symmetrical': 'False', 'to': "orm['filmography.Character']"}),
            'contributor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filmography.Contributor']"}),
            'costume_designers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'costume_designer_films'", 'symmetrical': 'False', 'to': "orm['filmography.Character']"}),
            'countries': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'create_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'designers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'designer_films'", 'symmetrical': 'False', 'to': "orm['filmography.Character']"}),
            'directors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'director_films'", 'symmetrical': 'False', 'to': "orm['filmography.Character']"}),
            'editors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'editor_films'", 'symmetrical': 'False', 'to': "orm['filmography.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'null': 'True', 'blank': 'True'}),
            'is_color': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'languages': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'mediums': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['filmography.FilmMedium']", 'symmetrical': 'False'}),
            'musicians': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'musician_films'", 'symmetrical': 'False', 'to': "orm['filmography.Character']"}),
            'producers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'producer_films'", 'symmetrical': 'False', 'to': "orm['filmography.Character']"}),
            'production': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'publish_date': ('django.db.models.fields.IntegerField', [], {}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'release_date': ('django.db.models.fields.IntegerField', [], {}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'films'", 'symmetrical': 'False', 'to': "orm['filmography.FilmType']"}),
            'update_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'filmography.filmcharacter': {
            'Meta': {'object_name': 'FilmCharacter'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filmography.Character']"}),
            'film': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filmography.Film']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'filmography.filmmedium': {
            'Meta': {'object_name': 'FilmMedium'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'filmography.filmtype': {
            'Meta': {'object_name': 'FilmType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'filmography.play': {
            'Meta': {'object_name': 'Play'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['filmography']
