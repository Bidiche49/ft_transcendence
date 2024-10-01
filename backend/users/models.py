from django.db import models

class User(models.Model):
	username = models.CharField(max_length=255, unique=True)
	email = models.EmailField(unique=True)
	password_hash = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	high_score = models.IntegerField(default=0)

	#Check if are utils :
	is_admin = models.BooleanField(default=False)
	nb_games = models.IntegerField(default=0)
	nb_victories = models.IntegerField(default=0)
	nb_defeats = models.IntegerField(default=0)
	nb_ties = models.IntegerField(default=0)

	def __str__(self):
		return self.username
