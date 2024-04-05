from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tournoi/<int:tournoi_id>/', views.tournoi_detail, name='tournoi_detail'),
    path('tournoi/<int:tournoi_id>/classement/', views.classement, name='classement'),
    path('tournoi/<int:tournoi_id>/historique/', views.historique, name='historique'),
    path('tournoi/<int:tournoi_id>/supprimer/', views.supprimer_tournoi, name='supprimer_tournoi'),
    path('tournoi/<int:tournoi_id>/participant/<int:participant_id>/supprimer/', views.supprimer_participant, name='supprimer_participant'),
    path('tournoi/<int:tournoi_id>/match/<int:match_id>/supprimer/', views.supprimer_match, name='supprimer_match'),
    path('tournoi/<int:tournoi_id>/match/<int:match_id>/modifier/', views.modifier_match, name='modifier_match'),
]