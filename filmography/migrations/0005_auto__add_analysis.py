# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Analysis'
        db.create_table('filmography_analysis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('filmography', ['Analysis'])

        # Adding M2M table for field films on 'Analysis'
        db.create_table('filmography_analysis_films', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('analysis', models.ForeignKey(orm['filmography.analysis'], null=False)),
            ('film', models.ForeignKey(orm['filmography.film'], null=False))
        ))
        db.create_unique('filmography_analysis_films', ['analysis_id', 'film_id'])

        # Adding M2M table for field contributors on 'Analysis'
        db.create_table('filmography_analysis_contributors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('analysis', models.ForeignKey(orm['filmography.analysis'], null=False)),
            ('contributor', models.ForeignKey(orm['filmography.contributor'], null=False))
        ))
        db.create_unique('filmography_analysis_contributors', ['analysis_id', 'contributor_id'])


    def backwards(self, orm):
        
        # Deleting model 'Analysis'
        db.delete_table('filmography_analysis')

        # Removing M2M table for field films on 'Analysis'
        db.delete_table('filmography_analysis_films')

        # Removing M2M table for field contributors on 'Analysis'
        db.delete_table('filmography_analysis_contributors')


    models = {
        'filmography.analysis': {
            'Meta': {'object_name': 'Analysis'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'contributors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['filmography.Contributor']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'films': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['filmography.Film']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'image': ('filebrowser.fields.FileBrowseField', [], {}),
            'is_color': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'languages': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'mediums': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['filmography.FilmMedium']", 'symmetrical': 'False'}),
            'musicians': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'musician_films'", 'symmetrical': 'False', 'to': "orm['filmography.Character']"}),
            'producers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'producer_films'", 'symmetrical': 'False', 'to': "orm['filmography.Character']"}),
            'production': ('django.db.models.fields.TextField', [], {}),
            'publish_date': ('django.db.models.fields.DateField', [], {}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'release_date': ('django.db.models.fields.DateField', [], {}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'films'", 'symmetrical': 'False', 'to': "orm['filmography.FilmType']"}),
            'update_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'writers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'writer_films'", 'symmetrical': 'False', 'to': "orm['filmography.Character']"})
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
        }
    }

    complete_apps = ['filmography']
