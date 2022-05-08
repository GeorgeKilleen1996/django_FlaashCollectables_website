from django.contrib import admin
from .models import PokemonSingle
from .models import PokemonSet

admin.site.register(PokemonSingle)
admin.site.register(PokemonSet)
