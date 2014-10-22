# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Game.tournament_points_white'
        db.add_column(u'chess_tournaments_game', 'tournament_points_white',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Game.tournament_points_black'
        db.add_column(u'chess_tournaments_game', 'tournament_points_black',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Game.tournament_points_white'
        db.delete_column(u'chess_tournaments_game', 'tournament_points_white')

        # Deleting field 'Game.tournament_points_black'
        db.delete_column(u'chess_tournaments_game', 'tournament_points_black')


    models = {
        u'chess_tournaments.game': {
            'Meta': {'object_name': 'Game'},
            'elo_gained_black': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'elo_gained_white': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_game_in_tour': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'number_of_tour': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'opponent_black': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'opponent_black'", 'null': 'True', 'to': u"orm['chess_tournaments.Participant']"}),
            'opponent_white': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'opponent_white'", 'null': 'True', 'to': u"orm['chess_tournaments.Participant']"}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chess_tournaments.Tournament']"}),
            'tournament_points_black': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'tournament_points_white': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'winner': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'})
        },
        u'chess_tournaments.participant': {
            'Meta': {'object_name': 'Participant'},
            'age': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'elo_rating': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'chess_tournaments.tournament': {
            'Meta': {'object_name': 'Tournament'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tournament_participants'", 'symmetrical': 'False', 'to': u"orm['chess_tournaments.Participant']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['chess_tournaments']