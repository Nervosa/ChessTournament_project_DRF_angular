from chess_tournaments.models import Participant, Tournament, Game
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("password", "first_name", "last_name", "email", "username")
        write_only_fields = ("password",)

    def restore_object(self, attrs, instance=None):
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user


class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(ParticipantSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Participant
        fields = ['id', 'name', 'surname', 'age', 'elo_rating']


class TournamentSerializer(serializers.HyperlinkedModelSerializer):
    # game_set = serializers.HyperlinkedRelatedField(queryset=Game.objects.all(), many=True, view_name='game-detail')

    class Meta:
        model = Tournament
        fields = ['title', 'start_date', 'end_date']


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['tournament', 'number_of_tour', 'opponent_white', 'opponent_black', 'winner',
                  'elo_gained_white', 'elo_gained_black']