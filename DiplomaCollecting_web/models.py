from django.db import models

# Create your models here.
class Datebase(models.Model):
    exam = models.CharField(max_length= 100)
    e_time = models.CharField(max_length=100)
    e_fee = models.CharField(max_length=100)
    e_applytime = models.CharField(max_length=100)
    e_searchscore = models.CharField(max_length=100)
    e_official_web = models.CharField(max_length=100)
