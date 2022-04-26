from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Home Page
def index(response):
	return HttpResponse("<h1>Home</h1>")

# Pokemon Section
def pokemonhome(response):
	return HttpResponse("<h1>pokemon home</h1>")

def pokemonsingles(response):
	return HttpResponse("<h1>singles</h1>")

def pokemonbundles(response):
	return HttpResponse("<h1>bundles</h1>")

def pokemonsealedproduct(response):
	return HttpResponse("<h1>sealed product</h1>")

def pokemongradedcards(response):
	return HttpResponse("<h1>graded cards</h1>")

def pokemonaccessories(response):
	return HttpResponse("<h1>accessories</h1>")