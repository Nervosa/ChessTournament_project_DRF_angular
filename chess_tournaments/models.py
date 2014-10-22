from django.core.exceptions import ValidationError
from django.db import models


class Participant(models.Model):

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    elo_rating = models.FloatField(default=0.0)

    def __unicode__(self):
        return u"%s" % self.surname+" "+self.name+"("+str(self.elo_rating)+")"


class Tournament(models.Model):

    title = models.CharField(max_length=150)
    start_date = models.DateField(verbose_name="Start date")
    end_date = models.DateField(verbose_name="End date")
    participants = models.ManyToManyField(Participant, related_name='tournament_participants')
    is_over = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s" % self.title

    def save(self, *args, **kwargs):
        if self.start_date > self.end_date:
            raise ValidationError("Verify terms of tournament.")
        super(Tournament, self).save(*args, **kwargs)


class Game(models.Model):

    tournament = models.ForeignKey(Tournament, related_name='game_set')
    number_of_tour = models.PositiveSmallIntegerField()
    number_of_game_in_tour = models.PositiveSmallIntegerField()
    opponent_white = models.ForeignKey(Participant, related_name='opponent_white', blank=True, null=True)
    opponent_black = models.ForeignKey(Participant, related_name='opponent_black', blank=True, null=True)
    winner = models.CharField(max_length=150, choices=(('White', 'White'), ('Black', 'Black'), ('Draw', 'Draw')), blank=True)
    elo_gained_white = models.FloatField(default=0.0)
    elo_gained_black = models.FloatField(default=0.0)

    def __unicode__(self):
        return u'Game %i' % self.number_of_game_in_tour + u' of tour %i' % self.number_of_tour + u' of tournament \"%s' % self.tournament + '\"'

    def save(self, *args, **kwargs):
        super(Game, self).save(*args, **kwargs)
        if self.opponent_black == self.opponent_white:
            raise ValidationError("Player \"" + self.opponent_white.surname + " " + self.opponent_white.name + "\" is duplicated in game#" + str(self.number_of_game_in_tour) + " of tour#" + str(self.number_of_tour))

    def clean(self, *args, **kwargs):
        super(Game, self).clean(*args, **kwargs)