from rest_framework.response import Response
from rest_framework.views import APIView
from chess_tournaments.api.serializers import ParticipantSerializer, TournamentSerializer, GameSerializer, UserSerializer
from .permissions import IsStaffOrTargetUser
from rest_framework import permissions, generics, views
from rest_framework.response import Response
from chess_tournaments.models import Participant
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .authentication import ChessTournamentBasicAuthentication


class AuthView(views.APIView):
    authentication_classes = (ChessTournamentBasicAuthentication,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return Response(self.serializer_class(request.user).data)


class UserView(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    model = User

    def get_permissions(self):
        return (AllowAny() if self.request.method == 'POST' else IsStaffOrTargetUser()),


class ParticipantList(generics.ListCreateAPIView):

    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ParticipantDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)