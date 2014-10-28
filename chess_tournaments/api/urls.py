from django.conf.urls import patterns, url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from chess_tournaments.api import views


router = routers.DefaultRouter()
router.register(r'accounts',views.UserView, 'user-list')


urlpatterns = patterns('chess_tournaments.api',
    url(r'^api/participants/$', views.ParticipantList.as_view()),
    url(r'^api/participants/(?P<pk>[0-9]+)/$', views.ParticipantDetail.as_view()),
    url(r'^api/auth/$', views.AuthView.as_view(), name='authenticate'),
    url(r'^api/', include(router.urls)),
)

# urlpatterns = format_suffix_patterns(urlpatterns)