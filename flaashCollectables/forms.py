from django import forms
from django.forms import ModelForm
from .models import SellToUsForm

#Creating the Sell To Us Form

class SellingForm(ModelForm):
	class Meta:
		model = SellToUsForm
		fields = ('firstName', 'lastName', 'emailAddress', 'addressLine1', 'city',
 				'postCode', 'cucCards', 'rCards', 'rholoCards', 'holoCards', 
 				'specialCards', 'vCards', 'energyCards', 'trainerCards', 'totalCards')
		labels = {
			'firstName' : '',
			'lastName' : '', 
			'emailAddress' : '', 
			'addressLine1' : '', 
			'city' : '', 
			'postCode' : '', 
			'cucCards' : 'Number of Common/Uncommon Cards - £0.02 per card', 
			'rCards' : 'Number of Rare Cards - £0.05 per card', 
			'rholoCards' : 'Number of Reverse Holos - £0.10 per card:', 
			'holoCards' : 'Number of Holos - £0.20 per card:', 
			'specialCards' : 'Number of EXs, GXs, Full Arts or VMAXs - £1.25 per card:', 
			'vCards' : 'Number of V Cards - £0.80 per card:', 
			'energyCards' : 'Number of Energy Cards - £0.005 per card:',
			'trainerCards' : 'Number of Trainer Cards - £0.02 per card:', 
			'totalCards' : 'Total Number of Cards Submitted:', 
		}
		widgets = {
			'firstName' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
			'lastName' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}), 
			'emailAddress' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address (Same as Paypal address)'}), 
			'addressLine1' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address Line'}), 
			'city' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), 
			'postCode' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Post Code'}), 
			'cucCards' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'# Common/Uncommon Cards'}), 
			'rCards' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'# Rare Cards'}), 
			'rholoCards' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'# Reverse Holo Cards'}), 
			'holoCards' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'# Holo Cards'}), 
			'specialCards' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'# EX, GX, Full Art, VMAX Cards'}), 
			'vCards' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'# V Cards'}), 
			'energyCards' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'# Energy Cards'}),
			'trainerCards' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'# Trainer Cards'}), 
			'totalCards' : forms.DateInput(attrs={'class':'form-control', 'placeholder':'Total Number of Cards'}), 
		}