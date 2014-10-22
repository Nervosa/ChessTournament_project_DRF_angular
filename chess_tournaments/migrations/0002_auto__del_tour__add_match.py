# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Tour'
        db.delete_table(u'chess_tournaments_tour')

        # Adding model 'Match'
        db.create_table(u'chess_tournaments_match', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tournament', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chess_tournaments.Tournament'])),
            ('number_of_tour', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('opponent_white', self.gf('django.db.models.fields.related.ForeignKey')(related_name='opponent_white', to=orm['chess_tournaments.Participant'])),
            ('opponent_black', self.gf('django.db.models.fields.related.ForeignKey')(related_name='opponent_black', to=orm['chess_tournaments.Participant'])),
            ('winner', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'chess_tournaments', ['Match'])


    def backwards(self, orm):
        # Adding model 'Tour'
        db.create_table(u'chess_tournaments_tour', (
            ('progress', self.gf('jsonfield.fields.JSONField')()),
            ('number_of_tour', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tournament', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chess_tournaments.Tournament'])),
        ))
        db.send_create_signal(u'chess_tournaments', ['Tour'])

        # Deleting model 'Match'
        db.delete_table(u'chess_tournaments_match')


    models = {
        u'chess_tournaments.match': {
            'Meta': {'object_name': 'Match'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_tour': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'opponent_black': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'opponent_black'", 'to': u"orm['chess_tournaments.Participant']"}),
            'opponent_white': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'opponent_white'", 'to': u"orm['chess_tournaments.Participant']"}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chess_tournaments.Tournament']"}),
            'winner': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'chess_tournaments.participant': {
            'Meta': {'object_name': 'Participant'},
            'age': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'elo_rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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