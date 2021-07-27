from django.db import models


# Create your models here.

class GameInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, null=False)
    time = models.IntegerField(null=True)
    difficulty = models.FloatField(null=True)
    counts = models.IntegerField(default=0, null=False)


class IgdbLink(models.Model):
    igdb_id = models.IntegerField(primary_key=True)
    game_id = models.OneToOneField(GameInfo, on_delete=models.CASCADE)


class GameSubmissions(models.Model):
    sub_id = models.BigAutoField(primary_key=True)
    game = models.ForeignKey(GameInfo, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    time = models.IntegerField(null=False)
    difficulty = models.FloatField(null=False)
