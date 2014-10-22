from chess_tournaments.api.serializers import ParticipantSerializer, TournamentSerializer, GameSerializer
from chess_tournaments.models import Participant, Tournament, Game
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from chess_tournaments.models import Participant
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def participants_list(request, format=None):
    if request.method == 'GET':
        participants = Participant.objects.all()
        participants_serializer = ParticipantSerializer(participants, many=True)
        return Response(participants_serializer.data)
    elif request.method == 'POST':
        participants_serializer = ParticipantSerializer(data=request.data)
        if participants_serializer.is_valid():
            participants_serializer.save()
            return Response(participants_serializer.data, status=status.HTTP_201_CREATED)
        return Response(participants_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def participant_detail(request, pk, format=None):
    try:
        participant = Participant.objects.get(pk=pk)
    except Participant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        participants_serializer = ParticipantSerializer(participant)
        return Response(participants_serializer.data)

    elif request.method == 'PUT':
        participants_serializer = ParticipantSerializer(participant, request.DATA, partial=True)
        if participants_serializer.is_valid():
            participants_serializer.save()
            return Response(participants_serializer.data)
        return Response(participants_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        participant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class ParticipantList(generics.ListCreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class ParticipantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    def put(self, request, *args, **kwargs):
        pass



class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    '''

