from django.contrib import admin
from django.urls import path
from .views import ajouter, ajoumariage, ajoudeces, rechercher_persone, rechercher_mariage, recherche_deces, edit, update, venue_pdf, extrait_pdf, extrait_mariage, extrait_deces, statistique


urlpatterns = [
   
    path('ajouter/', ajouter, name='ajouter'), 
    path('ajoumariage/', ajoumariage, name='ajoumariage'),
    path('ajoudeces/', ajoudeces, name='ajoudeces'),
    path('rechercher_persone/', rechercher_persone, name='rechercher_persone'),
    path('rechercher_mariage/', rechercher_mariage, name='rechercher_mariage'),
    path('rechercher_deces/', recherche_deces, name='rechercher_deces'),
    path('edit/<int:id>/', edit, name='edit'),
    path('update/<int:id>/', update, name='update'),
    path('venue_pdf/', venue_pdf, name='venue_pdf'),
    path('extrait_pdf/<int:id>/', extrait_pdf, name='extrait_pdf'),
    path('extrait_mariage/<int:id>/', extrait_mariage, name='extrait_mariage'),
    path('extrait_deces/<int:id>/', extrait_deces, name='extrait_deces'),
    path('statistique/', statistique, name='statistique'),
]