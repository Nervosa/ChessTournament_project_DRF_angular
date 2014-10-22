from django.conf.urls import patterns, url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('chess_tournaments.api.views',
    url(r'^api/participants/$', 'participants_list'),
    url(r'^api/participants/(?P<pk>[0-9]+)$', 'participant_detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)





'''
router = routers.DefaultRouter()
router.register(r'participants', ParticipantViewSet)
router.register(r'tournaments', TournamentViewSet)
router.register(r'games', GameViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^participants_view/$', ParticipantList.as_view()),
    url(r'^participants_view/(?P<pk>[0-9]+)/$', ParticipantDetail.as_view())
)

# urlpatterns = format_suffix_patterns(urlpatterns)
'''