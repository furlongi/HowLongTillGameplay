from django.db import models, transaction, IntegrityError
from utils.helpers import filter_array_json


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


# Helper Methods

def add_new_titles(array):
    ids = filter_array_json('id', array)
    found_games_ids = {i.igdb_id for i in IgdbLink.objects.filter(pk__in=ids)}
    missing_ids = [entry for entry in array if entry['id'] not in found_games_ids]
    gameinfo_inserts = [GameInfo(name=entry['name']) for entry in missing_ids]

    for i, game in enumerate(gameinfo_inserts):
        try:
            with transaction.atomic():
                game.save(force_insert=True)
                local_id = GameInfo.objects.latest('id')
                obj = missing_ids[i]
                link = IgdbLink(igdb_id=obj['id'], game_id=local_id)
                link.save(force_insert=True)
        except IntegrityError:
            continue
