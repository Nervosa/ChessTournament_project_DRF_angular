from models import Game


def get_games_and_tours(tournament_id):
    games = Game.objects.filter(tournament=tournament_id).order_by('number_of_game_in_tour', 'number_of_tour')
    num_of_tours = games.values('number_of_tour').distinct().count()
    if games.count() == 0:
        games = None
        num_of_tours = None
    return games, num_of_tours


def get_participants_tournament_points(participants, games):

    tournament_points = {participant: 0 for participant in participants}
    if games:
        for participant in participants:
            for game in games:
                if game.opponent_white == participant and game.winner == 'White':
                    tournament_points[participant] += 1
                if game.opponent_black == participant and game.winner == 'Black':
                    tournament_points[participant] += 1
                if (game.opponent_black == participant or game.opponent_white == participant) and game.winner == 'Draw':
                    tournament_points[participant] += 0.5
                if (not game.opponent_black and game.opponent_white == participant) or (not game.opponent_white and game.opponent_black == participant):
                    tournament_points[participant] += 1

    return sorted(tournament_points.items(), key=lambda t: t[1], reverse=True)


def calculate_elo_earned(game):

    what_changed = game.changed_data
    cleaned_data = game.cleaned_data
    if len(what_changed) == 0 or not cleaned_data['opponent_black'] or not cleaned_data['opponent_white']:
        return
    elif not cleaned_data['winner']:
        game.instance.elo_gained_black = 0.0
        game.instance.elo_gained_white = 0.0
    else:
        elo_black = cleaned_data['opponent_black'].elo_rating
        elo_white = cleaned_data['opponent_white'].elo_rating
        expectation_value_black = 1/(1 + pow(10, (elo_white-elo_black)/400.0))
        expectation_value_white = 1/(1 + pow(10, (elo_black-elo_white)/400.0))
        if elo_black >= 2400.0:
            k_black = 10.0
        elif elo_black < 2400.0:
            k_black = 15.0

        if elo_white >= 2400.0:
            k_white = 10.0
        elif elo_white < 2400.0:
            k_white = 15.0

        if cleaned_data['winner'] == 'Black':
            s_black = 1.0
            s_white = 0.0
        if cleaned_data['winner'] == 'White':
            s_black = 0.0
            s_white = 1.0
        if cleaned_data['winner'] == 'Draw':
            s_black = 0.5
            s_white = 0.5

        game.instance.elo_gained_white = round(k_white*(s_white - expectation_value_white), 2)
        game.instance.elo_gained_black = round(k_black*(s_black - expectation_value_black), 2)
