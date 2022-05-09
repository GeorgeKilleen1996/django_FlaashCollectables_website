from django.urls import path

from . import views 

urlpatterns = [
# Flaash Collectables Home
path("", views.home, name="index"),
# Pokemon Section
path("pokemonsingles", views.pokemonsingles, name="pokemonsingles"),
path("pokemonsealedproduct", views.pokemonsealedproduct, name="pokemonsealedproduct"),
path("pokemongradedcards", views.pokemongradedcards, name="pokemongradedcards"),
path("pokemonbundles", views.pokemonbundles, name="pokemonbundles"),
# Sports section
path("sportssinglecards", views.sportssinglecards, name="sportssinglecards"),
path("sportssinglestickers", views.sportssinglestickers, name="sportssinglestickers"),
path("sportsgradedcards", views.sportsgradedcards, name="sportsgradedcards"),
path("sportssealedproduct", views.sportssealedproduct, name="sportssealedproduct"),
# Funko section
path("funko", views.funko, name="funko"),
# Other section
path("magicthegathering", views.magicthegathering, name="magicthegathering"),
path("yugioh", views.yugioh, name="yugioh"),
# Accessories section
path("accessories", views.accessories, name="accessories"),
# Sale section
path("sale", views.sale, name="sale"),
# Coming Soon section
path("comingsoon", views.comingsoon, name="comingsoon"),

# Sell To Us section
path("selltous", views.selltous, name="selltous"),
]