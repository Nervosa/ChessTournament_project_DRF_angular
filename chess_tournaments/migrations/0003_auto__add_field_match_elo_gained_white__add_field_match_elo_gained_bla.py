# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Match.elo_gained_white'
        db.add_column(u'chess_tournaments_match', 'elo_gained_white',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Match.elo_gained_black'
        db.add_column(u'chess_tournaments_match', 'elo_gained_black',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Match.elo_gained_white'
        db.delete_column(u'chess_tournaments_match', 'elo_gained_white')

        # Deleting field 'Match.elo_gained_black'
        db.delete_column(u'chess_tournaments_match', 'elo_gained_black')


    models = {
        u'chess_tournaments.match': {
            'Meta': {'object_name': 'Match'},
            'elo_gained_black': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'elo_gained_white': ('django.db.models.fields.FloatField', [], {'default': '0'}),
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