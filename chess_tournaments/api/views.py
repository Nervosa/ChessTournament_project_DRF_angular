from bsddb import _iter_mixin
from django.http.response import Http404
from rest_framework.views import APIView
from chess_tournaments.api.serializers import ParticipantSerializer, TournamentSerializer, GameSerializer
from chess_tournaments.models import Participant, Tournament, Game
from rest_framework import viewsets, mixins
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from chess_tournaments.models import Participant
from rest_framework.decorators import api_view


class ParticipantList(generics.ListCreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class ParticipantDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer