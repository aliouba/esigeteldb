from django.db import models
from django.contrib.auth.models import User
class UserEntreprise(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(null=True,max_length=30)
	ref = models.CharField(null=True,max_length=30)
	siret = models.CharField(null=True,max_length=30)
	slogan = models.CharField(null=True,max_length=30)
	type_forfait = models.CharField(null=True,max_length=30)
	date_creation_entreprise = models.DateField(null=True)		
	domaine = models.CharField(null=True,max_length=30)
	logo = models.ImageField(null=True,upload_to="logo/userentreprise")
	def __unicode__(self):
		return u"%s" % self.name
class Produit(models.Model):
	produit_name = models.CharField(max_length=30)
	produit_prix = models.DecimalField(max_digits=5, decimal_places=2)
	taxe = models.IntegerField(null=True)
	stock = models.IntegerField(null=True)
	produit_image = models.ImageField(null=True,blank=True,upload_to="logo/produit/")
	produit_entreprise = models.ForeignKey(UserEntreprise)
	def __unicode__(self):
		return self.produit_name
class Achats(models.Model):
	ref_achats = models.CharField(null=True,max_length=30)
	nombre = models.IntegerField(null=True)
	prixhtc = models.DecimalField(max_digits=5, decimal_places=2)
	prixttc = models.DecimalField(max_digits=5, decimal_places=2)
	produit = models.ForeignKey(Produit)
	def __unicode__(self):
		return self.ref_achats
