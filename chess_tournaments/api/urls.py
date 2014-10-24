from django.conf.urls import patterns, url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from chess_tournaments.api import views

urlpatterns = patterns('chess_tournaments.api',
    url(r'^api/participants/$', views.ParticipantList.as_view()),
    url(r'^api/participants/(?P<pk>[0-9]+)/$', views.ParticipantDetail.as_view()),
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