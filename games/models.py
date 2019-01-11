from django.db import models
from datetime import datetime
from users.models import CustomUser

# Create your models here.

class Fight(models.Model):
    boxer_1 = models.CharField(max_length=100)
    boxer_2 = models.CharField(max_length=100)
    fight_date = models.DateTimeField(blank=True, null= True, auto_now=False, auto_now_add=False)
    result = models.IntegerField(blank=True, null=True)

class Game(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fight_id = models.ForeignKey(Fight, on_delete=models.CASCADE)
    time_created = models.DateTimeField(datetime.now())
    time_finished = models.DateTimeField(blank=True, null= True, auto_now=False, auto_now_add=False)

class Round(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    round_number = models.IntegerField(blank=True, null=True)
    boxer_1_hits = models.IntegerField(blank=True, null=True)
    boxer_1_knockdowns = models.IntegerField(blank=True, null=True)
    boxer_1_penalties = models.IntegerField(blank=True, null=True)
    boxer_2_hits = models.IntegerField(blank=True, null=True)
    boxer_2_knockdowns = models.IntegerField(blank=True, null=True)
    boxer_2_penalties = models.IntegerField(blank=True, null=True)
