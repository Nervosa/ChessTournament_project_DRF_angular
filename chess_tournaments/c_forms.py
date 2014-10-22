from django import forms
from chess_tournaments.models import Participant, Tournament, Game


class TournamentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TournamentForm, self).__init__(*args, **kwargs)
        self.fields['participants'].help_text = ""

    class Meta:
        model = Tournament
        widgets = {'start_date': forms.DateInput(attrs={'id': 'start_date_datepicker', 'type': 'text'}),
                   'end_date': forms.DateInput(attrs={'id': 'end_date_datepicker', 'type': 'text'})}


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'surname', 'age', 'elo_rating']


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        widgets = {'opponent_white': forms.Select(attrs={'id': 'huy_white'}),
                   'opponent_black': forms.Select(attrs={'id': 'huy_black'})}