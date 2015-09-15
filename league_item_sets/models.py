from django.db import models
from django.conf import settings

# Create your models here.
class Item(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	api_id = models.IntegerField()
	parent_row = models.ForeignKey("ItemRow")

class ItemRow(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=64)
	parent_set = models.ForeignKey("ItemSet")

class ItemSet(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=64)
	creator = models.ForeignKey(settings.AUTH_USER_MODEL)

	ANY = "any"
	SR = "SR"
	TT = "TT"
	HA = "HA"
	CS = "CS"
	CLASSIC = "CLASSIC"
	ARAM = "ARAM"
	ODIN = "ODIN"

	MAP_CHOICES = (
		(ANY, "Any Map"),
		(SR, "Summoner's Rift"),
		(TT, "Twisted Treeline"),
		(HA, "Howling Abyss"),
		(CS, "Crystal Scar"),
	)
	GAME_TYPE_CHOICES = (
		(ANY, "Any Mode"),
		(CLASSIC, "Classic"),
		(ARAM, "ARAM"),
		(ODIN, "Dominion"),
	)
	map = models.CharField(
		max_length=4,
		choices=MAP_CHOICES,
		default="any",
	)
	game_type = models.CharField(
		max_length=8,
		choices=GAME_TYPE_CHOICES,
		default="any",
	)

	class Meta:
		verbose_name = "ItemSet"
		verbose_name_plural = "ItemSets"
		ordering = ['created_at',]

	def __str__(self):
		return self.name


