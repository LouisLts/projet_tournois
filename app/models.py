from django.db import models

class Tournoi(models.Model):
    nom = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return self.nom

class Participant(models.Model):
    nom = models.CharField(max_length=100)
    tournoi = models.ForeignKey(Tournoi, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Match(models.Model):
    tournoi = models.ForeignKey(Tournoi, on_delete=models.CASCADE)
    participant1 = models.ForeignKey(Participant, related_name='matchs_participant1', on_delete=models.CASCADE)
    participant2 = models.ForeignKey(Participant, related_name='matchs_participant2', on_delete=models.CASCADE)
    score1 = models.PositiveIntegerField()
    score2 = models.PositiveIntegerField()
    gagnant = models.ForeignKey(Participant, related_name='matchs_gagnes', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.participant1} vs {self.participant2}"