from django import forms
from .models import Tournoi, Participant, Match

class TournoiForm(forms.ModelForm):
    class Meta:
        model = Tournoi
        fields = ['nom', 'date_debut', 'date_fin']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
        }

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['nom']

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['participant1', 'participant2', 'score1', 'score2', 'gagnant']

    def __init__(self, *args, **kwargs):
        tournoi = kwargs.pop('tournoi', None)
        super().__init__(*args, **kwargs)
        if tournoi:
            self.fields['participant1'].queryset = Participant.objects.filter(tournoi=tournoi)
            self.fields['participant2'].queryset = Participant.objects.filter(tournoi=tournoi)
            self.fields['gagnant'].queryset = Participant.objects.filter(tournoi=tournoi)