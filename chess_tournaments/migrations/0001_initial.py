# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Participant'
        db.create_table(u'chess_tournaments_participant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('age', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('elo_rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'chess_tournaments', ['Participant'])

        # Adding model 'Tournament'
        db.create_table(u'chess_tournaments_tournament', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'chess_tournaments', ['Tournament'])

        # Adding M2M table for field participants on 'Tournament'
        m2m_table_name = db.shorten_name(u'chess_tournaments_tournament_participants')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tournament', models.ForeignKey(orm[u'chess_tournaments.tournament'], null=False)),
            ('participant', models.ForeignKey(orm[u'chess_tournaments.participant'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tournament_id', 'participant_id'])

        # Adding model 'Tour'
        db.create_table(u'chess_tournaments_tour', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tournament', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chess_tournaments.Tournament'])),
            ('number_of_tour', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('progress', self.gf('jsonfield.fields.JSONField')()),
        ))
        db.send_create_signal(u'chess_tournaments', ['Tour'])


    def backwards(self, orm):
        # Deleting model 'Participant'
        db.delete_table(u'chess_tournaments_participant')

        # Deleting model 'Tournament'
        db.delete_table(u'chess_tournaments_tournament')

        # Removing M2M table for field participants on 'Tournament'
        db.delete_table(db.shorten_name(u'chess_tournaments_tournament_participants'))

        # Deleting model 'Tour'
        db.delete_table(u'chess_tournaments_tour')


    models = {
        u'chess_tournaments.participant': {
            'Meta': {'object_name': 'Participant'},
            'age': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'elo_rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'chess_tournaments.tour': {
            'Meta': {'object_name': 'Tour'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_tour': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'progress': ('jsonfield.fields.JSONField', [], {}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chess_tournaments.Tournament']"})
        },
        u'chess_tournaments.tournament': {
            'Meta': {'object_name': 'Tournament'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['chess_tournaments.Participant']", 'symmetrical': 'False'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['chess_tournaments']