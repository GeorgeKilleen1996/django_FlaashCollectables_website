from django.shortcuts import render
from django.http import HttpResponse
from .models import PokemonSingle
from .forms import SellingForm
from django.http import HttpResponseRedirect

# Create your views here.

# Home Page
def index(response):
	return render(response, "flaashCollectables/base.html", {})

def home(response):
	return render(response, "flaashCollectables/home.html", {})

# Pokemon Section

def pokemonsingles(response):
	pokemonsingles_list = PokemonSingle.objects.all()
	return render(response, "flaashCollectables/pokemon/pokemonsingles.html", 
		{'pokemonsingles_list' : pokemonsingles_list})

def pokemonsealedproduct(response):
	return render(response, "flaashCollectables/pokemon/pokemonsealedproduct.html", {})

def pokemongradedcards(response):
	return render(response, "flaashCollectables/pokemon/pokemongradedcards.html", {})

def pokemonbundles(response):
	return render(response, "flaashCollectables/pokemon/pokemonbundles.html", {})

# Sports Section

def sportssinglecards(response):
	return render(response, "flaashCollectables/sports/sportssinglecards.html", {})

def sportssinglestickers(response):
	return render(response, "flaashCollectables/sports/sportssinglestickers.html", {})

def sportsgradedcards(response):
	return render(response, "flaashCollectables/sports/sportsgradedcards.html", {})

def sportssealedproduct(response):
	return render(response, "flaashCollectables/sports/sportssealedproduct.html", {})

# Funko Section

def funko(response):
	return render(response, "flaashCollectables/funko.html", {})

# Other Section

def magicthegathering(response):
	return render(response, "flaashCollectables/other/magicthegathering.html", {})

def yugioh(response):
	return render(response, "flaashCollectables/other/yugioh.html", {})

# Accessories Section

def accessories(response):
	return render(response, "flaashCollectables/accessories.html", {})

# Sale Section

def sale(response):
	return render(response, "flaashCollectables/sale.html", {})

# Coming Soon Section

def comingsoon(response):
	return render(response, "flaashCollectables/comingsoon.html", {})

# Sell To Us Section

def selltous(request):
	submitted = False
	if request.method == "POST":
		form = SellingForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/selltous?submitted=True')
	else:
		form = SellingForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, "flaashCollectables/selltous.html", {'form' : form, 'submitted' : submitted })
