# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Film'
        db.create_table('filmography_film', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title_fr', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('production', self.gf('django.db.models.fields.TextField')()),
            ('length', self.gf('django.db.models.fields.IntegerField')()),
            ('countries', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('languages', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('release_date', self.gf('django.db.models.fields.DateField')()),
            ('publish_date', self.gf('django.db.models.fields.DateField')()),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('filebrowser.fields.CharField')(max_length=255)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('is_color', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('contributor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filmography.Contributor'])),
            ('create_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('filmography', ['Film'])

        # Adding M2M table for field directors on 'Film'
        db.create_table('filmography_film_directors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['filmography.film'], null=False)),
            ('character', models.ForeignKey(orm['filmography.character'], null=False))
        ))
        db.create_unique('filmography_film_directors', ['film_id', 'character_id'])

        # Adding M2M table for field writers on 'Film'
        db.create_table('filmography_film_writers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['filmography.film'], null=False)),
            ('character', models.ForeignKey(orm['filmography.character'], null=False))
        ))
        db.create_unique('filmography_film_writers', ['film_id', 'character_id'])

        # Adding M2M table for field cinematographers on 'Film'
        db.create_table('filmography_film_cinematographers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['filmography.film'], null=False)),
            ('character', models.ForeignKey(orm['filmography.character'], null=False))
        ))
        db.create_unique('filmography_film_cinematographers', ['film_id', 'character_id'])

        # Adding M2M table for field editors on 'Film'
        db.create_table('filmography_film_editors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['filmography.film'], null=False)),
            ('character', models.ForeignKey(orm['filmography.character'], null=False))
        ))
        db.create_unique('filmography_film_editors', ['film_id', 'character_id'])

        # Adding M2M table for field musicians on 'Film'
        db.create_table('filmography_film_musicians', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['filmography.film'], null=False)),
            ('character', models.ForeignKey(orm['filmography.character'], null=False))
        ))
        db.create_unique('filmography_film_musicians', ['film_id', 'character_id'])

        # Adding M2M table for field designers on 'Film'
        db.create_table('filmography_film_designers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['filmography.film'], null=False)),
            ('character', models.ForeignKey(orm['filmography.character'], null=False))
        ))
        db.create_unique('filmography_film_designers', ['film_id', 'character_id'])

        # Adding M2M table for field costume_designers on 'Film'
        db.create_table('filmography_film_costume_designers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['filmography.film'], null=False)),
            ('character', models.ForeignKey(orm['filmography.character'], null=False))
        ))
        db.create_unique('filmography_film_costume_designers', ['film_id', 'character_id'])

        # Adding M2M table for field producers on 'Film'
        db.create_table('filmography_film_producers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['filmography.film'], null=False)),
            ('character', models.ForeignKey(orm['filmography.character'], null=False))
        ))
        db.create_unique('filmography_film_producers', ['film_id', 'character_id'])

        # Adding M2M table for field mediums on 'Film'
        db.create_table('filmography_film_mediums', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['filmography.film'], null=False)),
            ('filmmedium', models.ForeignKey(orm['filmography.filmmedium'], null=False))
        ))
        db.create_unique('filmography_film_mediums', ['film_id', 'filmmedium_id'])

        # Adding M2M table for field types on 'Film'
        db.create_table('filmography_film_types', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['filmography.film'], null=False)),
            ('filmtype', models.ForeignKey(orm['filmography.filmtype'], null=False))
        ))
        db.create_unique('filmography_film_types', ['film_id', 'filmtype_id'])

        # Adding model 'FilmType'
        db.create_table('filmography_filmtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('reference', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('filmography', ['FilmType'])

        # Adding model 'FilmCharacter'
        db.create_table('filmography_filmcharacter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('film', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filmography.Film'])),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filmography.Character'])),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('filmography', ['FilmCharacter'])

        # Adding model 'FilmMedium'
        db.create_table('filmography_filmmedium', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('reference', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('filmography', ['FilmMedium'])


    def backwards(self, orm):
        
        # Deleting model 'Film'
        db.delete_table('filmography_film')

        # Removing M2M table for field directors on 'Film'
        db.delete_table('filmography_film_directors')

        # Removing M2M table for field writers on 'Film'
        db.delete_table('filmography_film_writers')

        # Removing M2M table for field cinematographers on 'Film'
        db.delete_table('filmography_film_cinematographers')

        # Removing M2M table for field editors on 'Film'
        db.delete_table('filmography_film_editors')

        # Removing M2M table for field musicians on 'Film'
        db.delete_table('filmography_film_musicians')

        # Removing M2M table for field designers on 'Film'
        db.delete_table('filmography_film_designers')

        # Removing M2M table for field costume_designers on 'Film'
        db.delete_table('filmography_film_costume_designers')

        # Removing M2M table for field producers on 'Film'
        db.delete_table('filmography_film_producers')

        # Removing M2M table for field mediums on 'Film'
        db.delete_table('filmography_film_mediums')

        # Removing M2M table for field types on 'Film'
        db.delete_table('filmography_film_types')

        # Deleting model 'FilmType'
        db.delete_table('filmography_filmtype')

        # Deleting model 'FilmCharacter'
        db.delete_table('filmography_filmcharacter')

        # Deleting model 'FilmMedium'
        db.delete_table('filmography_filmmedium')


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
