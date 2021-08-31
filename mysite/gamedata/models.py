from django.db import models, transaction, IntegrityError
from utils.helpers import filter_array_json


# Create your models here.

class GameInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, null=False)
    time = models.IntegerField(null=True)
    difficulty = models.FloatField(null=True)
    counts = models.IntegerField(default=0, null=False)
    cover = models.URLField(null=True)


class IgdbLink(models.Model):
    igdb_id = models.IntegerField(primary_key=True)
    game = models.OneToOneField(GameInfo, on_delete=models.CASCADE)


class RawgLink(models.Model):
    rawg_id = models.IntegerField(primary_key=True)
    game = models.OneToOneField(GameInfo, on_delete=models.CASCADE)
    slug = models.CharField(max_length=256, null=True)


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
    games_to_inserts = [GameInfo(name=entry['name'], cover=format_image_url(entry["cover"]))
                        for entry in missing_ids]

    for i, game in enumerate(games_to_inserts):
        try:
            with transaction.atomic():
                game.save(force_insert=True)
                local_id = GameInfo.objects.latest('id')
                obj = missing_ids[i]
                link = IgdbLink(igdb_id=obj['id'], game=local_id)
                link.save(force_insert=True)
        except IntegrityError:
            continue


def add_new_titles_rawg(array):
    ids = filter_array_json('id', array)
    found_games_ids = {i.rawg_id for i in RawgLink.objects.filter(pk__in=ids)}
    missing_ids = [entry for entry in array if entry['id'] not in found_games_ids]
    games_to_inserts = [GameInfo(name=entry['name']) for entry in missing_ids]

    for i, game in enumerate(games_to_inserts):
        try:
            with transaction.atomic():
                game.save(force_insert=True)
                local_id = GameInfo.objects.latest('id')
                obj = missing_ids[i]
                link = RawgLink(rawg_id=obj['id'], game=local_id, slug=obj["slug"])
                link.save(force_insert=True)
        except IntegrityError:
            continue


def format_image_url(data):
    if data is None or "url" not in data:
        return None
    url = data["url"]
    return "https:" + url.replace("t_thumb", "t_cover_big")

