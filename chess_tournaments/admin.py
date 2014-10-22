from django.contrib import admin
from models import Tournament, Game, Participant

admin.site.register(Participant)
admin.site.register(Tournament)
admin.site.register(Game)