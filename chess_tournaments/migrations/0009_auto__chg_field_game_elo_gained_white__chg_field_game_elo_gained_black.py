# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Game.elo_gained_white'
        db.alter_column(u'chess_tournaments_game', 'elo_gained_white', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'Game.elo_gained_black'
        db.alter_column(u'chess_tournaments_game', 'elo_gained_black', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'Participant.elo_rating'
        db.alter_column(u'chess_tournaments_participant', 'elo_rating', self.gf('django.db.models.fields.FloatField')())

    def backwards(self, orm):

        # Changing field 'Game.elo_gained_white'
        db.alter_column(u'chess_tournaments_game', 'elo_gained_white', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=3))

        # Changing field 'Game.elo_gained_black'
        db.alter_column(u'chess_tournaments_game', 'elo_gained_black', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=3))

        # Changing field 'Participant.elo_rating'
        db.alter_column(u'chess_tournaments_participant', 'elo_rating', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=3))

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