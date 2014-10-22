import json
from c_utils import calculate_elo_earned, get_games_and_tours, get_participants_tournament_points
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.forms.models import modelformset_factory
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from chess_tournaments.c_forms import TournamentForm, ParticipantForm
from chess_tournaments.models import Tournament, Game, Participant
from django.db.models import Q
from django import forms


def Main(request):
    return render_to_response('main.html', RequestContext(request))


def TournamentsView(request):
    tournaments = Tournament.objects.all()
    return render_to_response('tournaments_list.html', RequestContext(request, {
        'tournaments': tournaments,
    }))


def TournamentDetailView(request, tournament_id=None):
    GamesFormSet = modelformset_factory(Game, extra=0)
    if request.method == 'POST' and request.user.is_active:
        if tournament_id is None:
            tournament_form = TournamentForm(request.POST)
        else:
            tournament_form = TournamentForm(request.POST, instance=get_object_or_404(Tournament, pk=tournament_id))
        if tournament_form.is_valid():
            callback_data = {}
            try:
                if ('participants' not in tournament_form.changed_data and tournament_form.instance.game_set.all().count() != 0) or tournament_form.instance.game_set.all().count() == 0:
                    tournament_form.save(commit=True)
                    callback_data['result'] = 'Tournament info successfully saved.'
                    callback_data['tournament_id'] = tournament_form.instance.id
                    return HttpResponse(json.dumps(callback_data), content_type='application/json', status=200)
                else:
                    callback_data['result'] = 'Tournament wasn\'t saved. \n'
                    callback_data['error_text'] = 'You cannot change participants list when tournament is started.'
                    return HttpResponse(json.dumps(callback_data), content_type='application/json', status=500)
            except ValidationError as e:
                callback_data['result'] = 'Tournament wasn\'t saved. \n'
                callback_data['error_text'] = e.message
                return HttpResponse(json.dumps(callback_data), content_type='application/json', status=500)
        else:
            return render_to_response('tournament_detail.html', RequestContext(request, {
                'tournament_form': tournament_form,
            }))
    else:
        if tournament_id is None:
            tournament_form = TournamentForm()
            return render_to_response('tournament_detail.html', RequestContext(request, {
                'tournament_form': tournament_form,
            }))

        elif request.user.is_active:
            current_tournament = get_object_or_404(Tournament, pk=tournament_id)
            is_over = current_tournament.is_over
            tournament_form = TournamentForm(instance=current_tournament)
            games, num_of_tours = get_games_and_tours(tournament_id)
            participants = current_tournament.participants.all()
            participants_by_points = get_participants_tournament_points(participants, games)
            list_of_gameformsets = []
            if games:
                for tour in range(1, num_of_tours+1):
                    gameformset = GamesFormSet(queryset=current_tournament.game_set.filter(number_of_tour=tour),
                                               prefix='tour_'+str(tour)+'_games')
                    for gameform in gameformset:
                        gameform.fields['opponent_black'].queryset = current_tournament.participants
                        gameform.fields['opponent_white'].queryset = current_tournament.participants
                        gameform.fields['opponent_black'].widget.choices.field.empty_label = None
                        gameform.fields['opponent_white'].widget.choices.field.empty_label = None
                    list_of_gameformsets.append(gameformset)
            else:
                list_of_gameformsets = None
            return render_to_response('tournament_detail.html', RequestContext(request, {
                'tournament_is_over': is_over,
                'tournament_form': tournament_form,
                'tournament_title': current_tournament.title,
                'tournament_id': tournament_id,
                'list_of_gameformsets': list_of_gameformsets,
                'participants_by_points': participants_by_points,
            }))
        else:
            tournament = get_object_or_404(Tournament, pk=tournament_id)
            is_over = tournament.is_over
            participants = tournament.participants.all()
            games, num_of_tours = get_games_and_tours(tournament_id)
            participants_by_points = get_participants_tournament_points(participants, games)
            tour_numbers = []
            if games:
                for i in range(num_of_tours):
                    tour_numbers.append(i+1)
            return render_to_response('tournament_detail.html', RequestContext(request, {
                'tournament_is_over': is_over,
                'tournament': tournament,
                'participants': participants,
                'games': games,
                'tour_numbers': tour_numbers,
                'participants_by_points': participants_by_points,
            }))


def start_continue_tournament(request):
    if request.method == 'POST':
        tournament_id = request.POST.get('tournament_id')
        current_tournament = Tournament.objects.get(id=tournament_id)
        participants_of_tournament = current_tournament.participants.all().order_by('-elo_rating')
        games, num_of_tours = get_games_and_tours(tournament_id)
        callback_data = {}
        if games:
            for game in Game.objects.filter(tournament=current_tournament):
                if not game.winner and game.opponent_black and game.opponent_white:
                    callback_data['error_text'] = "You haven\'t completed previous tours."
                    return HttpResponse(json.dumps(callback_data), content_type='application/json', status=500)

            participants_by_points = get_participants_tournament_points(participants_of_tournament, games)
            pairs = [tuple(participants_by_points[i:i+2]) for i in range(0, len(participants_by_points), 2)]

            for num_of_game_in_tour, pair in enumerate(pairs):
                try:
                    new_game = Game.objects.create(tournament=Tournament.objects.get(id=tournament_id),
                                                   opponent_white=pair[0][0],
                                                   opponent_black=pair[1][0],
                                                   number_of_tour=num_of_tours+1,
                                                   number_of_game_in_tour=num_of_game_in_tour+1)
                except IndexError:
                    new_game = Game.objects.create(tournament=Tournament.objects.get(id=tournament_id),
                                                   opponent_white=pair[0][0],
                                                   opponent_black=None,
                                                   number_of_tour=num_of_tours+1,
                                                   number_of_game_in_tour=num_of_game_in_tour+1)
                new_game.save()

            return HttpResponse('')
        else:
            list_ids = list(participant.id for participant in participants_of_tournament)
            pairs = [tuple(list_ids[i:i+2]) for i in range(0, len(list_ids), 2)]
            for num_of_game_in_tour, pair in enumerate(pairs):
                try:
                    new_game = Game.objects.create(tournament=Tournament.objects.get(id=tournament_id),
                                                   opponent_white=Participant.objects.get(id=pair[0]),
                                                   opponent_black=Participant.objects.get(id=pair[1]),
                                                   number_of_tour=1,
                                                   number_of_game_in_tour=num_of_game_in_tour+1)
                except IndexError:
                    new_game = Game.objects.create(tournament=Tournament.objects.get(id=tournament_id),
                                                   opponent_white=Participant.objects.get(id=pair[0]),
                                                   opponent_black=None,
                                                   number_of_tour=1,
                                                   number_of_game_in_tour=num_of_game_in_tour+1)
                new_game.save()
            return HttpResponse('')


def ParticipantsView(request):
    participants = Participant.objects.all()
    return render_to_response('participants_list.html', RequestContext(request, {
        'participants': participants,
    }))


def ParticipantDetailView(request, participant_id=None):

    if request.method == 'POST' and request.user.is_active:
        if participant_id is None:
            participant_form = ParticipantForm(request.POST)
        else:
            participant_form = ParticipantForm(request.POST, instance=get_object_or_404(Participant, pk=participant_id))
        if participant_form.is_valid():
            participant_form.save()
            return HttpResponseRedirect('/participants/')
        else:
            return render_to_response('participant_detail.html', RequestContext(request, {
                'participant_form': participant_form,
            }))
    else:
        if participant_id is None:
            participant_form = ParticipantForm()
            return render_to_response('participant_detail.html', RequestContext(request, {
                'participant_form': participant_form,
            }))
        elif request.user.is_active:
            participant_form = ParticipantForm(instance=get_object_or_404(Participant, pk=participant_id))
            return render_to_response('participant_detail.html', RequestContext(request, {
                'participant_form': participant_form,
            }))
        else:
            participant = get_object_or_404(Participant, pk=participant_id)
            return render_to_response('participant_detail.html', RequestContext(request, {
                'participant': participant,
            }))


def save_tour(request):
    GamesFormSet = modelformset_factory(Game)
    callback_data = {}
    games_participants = []
    if request.method == "POST": # and request.is_ajax():
        prefix = 'tour_'+str(request.POST.get('num_of_tour'))+'_games'
        saved_formset = GamesFormSet(request.POST, prefix=prefix)
        if saved_formset.is_valid():

            for game in saved_formset.forms:
                games_participants.append(game.instance.opponent_black)
                games_participants.append(game.instance.opponent_white)
            for participant in games_participants:
                if games_participants.count(participant) > 1:
                    callback_data['result'] = "Not saved!"
                    callback_data['error_text'] = "\nPlayer "+participant.surname+" " + \
                                                  participant.name + \
                                                  " is set as opponent in two or more games either " \
                                                  "is duplicated in a single game. Fix it please."
                    return HttpResponse(json.dumps(callback_data), content_type='application/json', status=500)
            for game in saved_formset.forms:
                calculate_elo_earned(game)
            callback_data['result'] = 'Successfully saved!'
            callback_data['tournament_id'] = request.POST['num_of_tournament']
            saved_formset.save()
            return HttpResponse(json.dumps(callback_data), content_type='application/json')


def Login(request):
    if request.method == 'POST' and request.is_ajax():
        data = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if not user is None and user.is_active:
            login(request, user)
            data['result'] = 'success'
        else:
            data['result'] = 'fail'
        return HttpResponse(json.dumps(data), content_type='application/json')


def Logout(request):
    current_url = request.META['HTTP_REFERER']
    logout(request)
    return HttpResponseRedirect(current_url)


def complete_tournament(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    for participant in list(tournament.participants.values()):
        participant = Participant.objects.get(id=participant['id'])
        games_of_participant = Game.objects.filter(Q(tournament=tournament_id) & (Q(opponent_black=participant) | Q(opponent_white=participant)))
        for game in games_of_participant:
            if game.opponent_black == participant:
                participant.elo_rating += game.elo_gained_black
            if game.opponent_white == participant:
                participant.elo_rating += game.elo_gained_white
            participant.save()
    tournament.is_over = True
    tournament.save()
    tournament.is_over = True
    return HttpResponseRedirect('/tournaments/')