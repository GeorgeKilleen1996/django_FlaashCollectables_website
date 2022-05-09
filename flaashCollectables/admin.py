from django.contrib import admin
from .models import PokemonSingle
from .models import PokemonSet
from .models import SellToUsForm

admin.site.register(PokemonSingle)
admin.site.register(PokemonSet)
admin.site.register(SellToUsForm)
