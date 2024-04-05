from django.contrib import admin
from .models import Tournoi, Participant, Match

admin.site.register(Tournoi)
admin.site.register(Participant)
admin.site.register(Match)