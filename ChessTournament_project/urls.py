from django.conf.urls import patterns, include, url
from django.contrib import admin
from chess_tournaments.views import MainAngView


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', "chess_tournaments.views.Main_1", name='main_1'),
                       url(r'^\w+/$', "chess_tournaments.views.Main_2", name='main_2'),
                       # url(r'^tournaments/$', 'chess_tournaments.views.TournamentsView', name='tournaments'),
                       # url(r'^tournament/(?P<tournament_id>\d+)/$', 'chess_tournaments.views.TournamentDetailView',
                       #     name='tournament_detail'),
                       url(r'^tournament_new/$', 'chess_tournaments.views.TournamentDetailView', name='tournament_new'),
                       url(r'^participant_new/$', 'chess_tournaments.views.ParticipantDetailView', name='participant_new'),
                       url(r'^participants/$', 'chess_tournaments.views.ParticipantsView', name='participants'),
                       url(r'^participant/(?P<participant_id>\d+)/$', 'chess_tournaments.views.ParticipantDetailView',
                            name='participant_detail'),
                       url(r'^login/$', 'chess_tournaments.views.Login', name='login'),
                       url(r'^logout/$', 'chess_tournaments.views.Logout', name='logout'),
                       url(r'^inplaceeditform/', include('inplaceeditform.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^start_continue_tournament/', 'chess_tournaments.views.start_continue_tournament',
                            name='start_continue_tournament'),
                       url(r'^get_tours/', 'chess_tournaments.views.get_games_and_tours', name='get_tours'),
                       url(r'^save_tour/', 'chess_tournaments.views.save_tour', name='save_tour'),
                       url(r'^complete_tournament/(?P<tournament_id>\d+)/$', 'chess_tournaments.views.complete_tournament', name='complete_tournament'),
                       url(r'^(?P<template_name>\w+).html/$', MainAngView.as_view()),
                       url(r'^', include('chess_tournaments.api.urls'))
                       )