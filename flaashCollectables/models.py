from django.db import models

# Create your models here.

class PokemonSet(models.Model):
	setName = models.CharField('Set Name', max_length=120)
	#setName = models.ForeignKey(PokemonSet, blank=True, null=True, on_delete=models.CASCADE)
	yearReleased = models.DateField('Released')

	def __str__(self):
		return self.setName

class PokemonSingle(models.Model):
	itemName = models.CharField('Item Name', max_length=200)
	#setName = models.CharField('Set Name', max_length=120)
	setName = models.ForeignKey(PokemonSet, blank=True, null=True, on_delete=models.CASCADE)
	description = models.TextField('Item Description', blank=True)
	image = models.ImageField('Item Image', upload_to="images/")
	rrp_price = models.DecimalField('Recommended Retail Price', max_digits=10, decimal_places=2)
	init_price = models.DecimalField('Initial Price', max_digits=10, decimal_places=2)
	sale_price = models.DecimalField('Sale Price', max_digits=10, decimal_places=2)
	on_sale = models.BooleanField('On Sale')
	size_index = models.IntegerField('Size Index')
	quantity = models.IntegerField('Quantity')

	def __str__(self):
		return self.itemName
