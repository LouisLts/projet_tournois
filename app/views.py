from django.shortcuts import render, redirect, get_object_or_404
from .models import Tournoi, Participant, Match
from .forms import TournoiForm, ParticipantForm, MatchForm

def index(request):
    tournois = Tournoi.objects.all()
    if request.method == 'POST':
        form = TournoiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TournoiForm()
    return render(request, 'app/index.html', {'tournois': tournois, 'form': form})

def tournoi_detail(request, tournoi_id):
    tournoi = get_object_or_404(Tournoi, pk=tournoi_id)
    participants = Participant.objects.filter(tournoi=tournoi)
    matchs = Match.objects.filter(tournoi=tournoi)
    if request.method == 'POST':
        form_participant = ParticipantForm(request.POST)
        form_match = MatchForm(request.POST)
        if form_participant.is_valid():
            participant = form_participant.save(commit=False)
            participant.tournoi = tournoi
            participant.save()
            return redirect('tournoi_detail', tournoi_id=tournoi.id)
        elif form_match.is_valid():
            match = form_match.save(commit=False)
            match.tournoi = tournoi
            match.save()
            return redirect('tournoi_detail', tournoi_id=tournoi.id)
    else:
        form_participant = ParticipantForm()
        form_match = MatchForm(tournoi=tournoi)
    return render(request, 'app/tournoi_detail.html', {'tournoi': tournoi, 'participants': participants, 'matchs': matchs, 'form_participant': form_participant, 'form_match': form_match})

def classement(request, tournoi_id):
    tournoi = get_object_or_404(Tournoi, pk=tournoi_id)
    participants = Participant.objects.filter(tournoi=tournoi)
    classement = []
    for participant in participants:
        nb_victoires = Match.objects.filter(tournoi=tournoi, gagnant=participant).count()
        classement.append((participant, nb_victoires))
    classement.sort(key=lambda x: x[1], reverse=True)
    return render(request, 'app/classement.html', {'tournoi': tournoi, 'classement': classement})

def historique(request, tournoi_id):
    tournoi = get_object_or_404(Tournoi, pk=tournoi_id)
    matchs = Match.objects.filter(tournoi=tournoi).order_by('-id')
    return render(request, 'app/historique.html', {'tournoi': tournoi, 'matchs': matchs})

def supprimer_tournoi(request, tournoi_id):
    tournoi = get_object_or_404(Tournoi, pk=tournoi_id)
    tournoi.delete()
    return redirect('index')

def supprimer_participant(request, tournoi_id, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    participant.delete()
    return redirect('tournoi_detail', tournoi_id=tournoi_id)

def supprimer_match(request, tournoi_id, match_id):
    match = get_object_or_404(Match, pk=match_id)
    match.delete()
    return redirect('tournoi_detail', tournoi_id=tournoi_id)

def modifier_match(request, tournoi_id, match_id):
    match = get_object_or_404(Match, pk=match_id)
    if request.method == 'POST':
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect('tournoi_detail', tournoi_id=tournoi_id)
    else:
        form = MatchForm(instance=match)
    return render(request, 'app/modifier_match.html', {'form': form, 'match': match})