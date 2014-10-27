from chess_tournaments.api.serializers import ParticipantSerializer, TournamentSerializer, GameSerializer
from rest_framework import permissions
from rest_framework import generics
from chess_tournaments.models import Participant



class ParticipantList(generics.ListCreateAPIView):

    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ParticipantDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
'''
class ParticipantList(APIView):

    def get(self, request, format=None):
        participants = Participant.objects.all()
        participants_serializer = ParticipantSerializer(participants, many=True)
        return Response(participants_serializer.data)

    def post(self, request, format=None):
        participants_serializer = ParticipantSerializer(data=request.DATA)
        if participants_serializer.is_valid():
            participants_serializer.save()
            return Response(participants_serializer.DATA, status=status.HTTP_201_CREATED)
        return Response(participants_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParticipantDetail(APIView):

    def get_object(self, pk):
        try:
            return Participant.objects.get(pk=pk)
        except Participant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        participant = self.get_object(pk)
        participant_serializer = ParticipantSerializer(participant)
        return Response(participant_serializer.DATA)

    def put(self, request, pk, format=None):
        participant = self.get_object(pk)
        participant_serializer = ParticipantSerializer(participant, request.DATA, partial=True)
        if participant_serializer.is_valid():
            participant_serializer.save()
            return Response(participant_serializer.data)
        return Response(participant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        participant = Participant.objects.get(pk)
        participant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

