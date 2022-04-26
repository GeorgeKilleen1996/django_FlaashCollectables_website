from django.urls import path

from . import views 

urlpatterns = [
# Flaash Collectables Home
path("", views.index, name="index"),
# Pokemon Section
path("pokemonhome", views.pokemonhome, name="pokemonhome"),
path("pokemonsingles", views.pokemonsingles, name="pokemonsingles"),
path("pokemonbundles", views.pokemonbundles, name="pokemonbundles"),
path("pokemonsealedproduct", views.pokemonsealedproduct, name="pokemonsealedproduct"),
path("pokemongradedcards", views.pokemongradedcards, name="pokemongradedcards"),
path("pokemonaccessories", views.pokemonaccessories, name="pokemonaccessories"),
]