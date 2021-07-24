from django.db import models


# Create your models here.

class GameInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, null=False)
    time = models.IntegerField(null=True)
    difficulty = models.FloatField(null=True)
    counts = models.IntegerField(default=0, null=False)
