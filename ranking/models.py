from django.db import models

# Create your models here.

class gameInfo(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Rankinf(models.Model):
    gameid = models.IntegerField(default=0)
    playername = models.TextField(blank=True)
    score = models.IntegerField(default=0)