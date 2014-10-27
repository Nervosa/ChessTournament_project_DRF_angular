from chess_tournaments.api.serializers import ParticipantSerializer, TournamentSerializer, GameSerializer
from rest_framework import permissions
from rest_framework import generics
from chess_tournaments.models import Participant, Tournament, Game


class ParticipantList(generics.ListCreateAPIView):

    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ParticipantDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class TournamentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)