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
    round_1 = models.CharField(max_length=25)
    round_2 = models.CharField(max_length=25)
    round_3 = models.CharField(max_length=25)
    round_4 = models.CharField(max_length=25)
    round_5 = models.CharField(max_length=25)
    round_6 = models.CharField(max_length=25)
    round_7 = models.CharField(max_length=25)
    round_8 = models.CharField(max_length=25)
    round_9 = models.CharField(max_length=25)
    round_10 = models.CharField(max_length=25)
    round_11 = models.CharField(max_length=25)
    round_12 = models.CharField(max_length=25)
