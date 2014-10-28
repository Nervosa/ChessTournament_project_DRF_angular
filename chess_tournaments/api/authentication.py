from rest_framework.authentication import BasicAuthentication


class ChessTournamentBasicAuthentication(BasicAuthentication):

    def authenticate_header(self, request):
        return 'xBasic realm={0}'.format(self.www_authenticate_realm)
