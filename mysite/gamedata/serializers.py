from rest_framework import serializers
from .models import GameInfo, IgdbLink, GameSubmissions


# Validators
def _validate_game(game):
    print(game)
    if type(game) is not int:
        raise serializers.ValidationError("Game must be a number.", code='invalid_type')
    if game < 1:
        raise serializers.ValidationError("Game must be greater than 0.", code='invalid_format')
    return game


def _validate_time(time):
    if type(time) is not int:
        raise serializers.ValidationError("Time must be a number.", code='invalid_type')
    if time < 0:
        raise serializers.ValidationError("Time must be between 0 and 5.", code='invalid_format')
    return time


def _validate_difficulty(difficulty):
    if type(difficulty) not in {int, float}:
        raise serializers.ValidationError("Difficulty must be a number.", code='invalid_type')
    if difficulty < 0 or difficulty > 5:
        raise serializers.ValidationError("Difficulty must be between 0 and 5.", code='invalid_format')
    return difficulty


# Serializers
class GameInfoSerializer(serializers.ModelSerializer):

    igdb_id = serializers.ReadOnlyField(source='igdblink.igdb_id')

    class Meta:
        model = GameInfo
        fields = [
            'id',
            'name',
            'time',
            'difficulty',
            'igdb_id',
            'cover'
        ]


class GameInfoContainerSerializer(serializers.Serializer):
    data = GameInfoSerializer(many=True)


class GameSubmissionSerializer(serializers.Serializer):
    game = serializers.IntegerField(validators=[_validate_game])
    time = serializers.IntegerField(validators=[_validate_time])
    difficulty = serializers.FloatField(validators=[_validate_difficulty])



# class GameSubmissionSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = GameSubmissions
#         fields = [
#             'game',
#             'time',
#             'difficulty'
#         ]
#
#     def validate_game(self, game):
#         print(game)
#         if type(game) not in {int, GameInfo}:
#             raise serializers.ValidationError("Game must be a number.", code='invalid_type')
#         if game < 1:
#             raise serializers.ValidationError("Game must be greater than 0.", code='invalid_format')
#         return game
#
#     def validate_time(self, time):
#         if type(time) is not int:
#             raise serializers.ValidationError("Time must be a number.", code='invalid_type')
#         if time < 0:
#             raise serializers.ValidationError("Time must be greater than or equal to 0.", code='invalid_format')
#         return time
#
#     def validate_difficulty(self, difficulty):
#         if type(difficulty) not in {int, float}:
#             raise serializers.ValidationError("Difficulty must be a number.", code='invalid_type')
#         if difficulty < 0 or difficulty > 5:
#             raise serializers.ValidationError("Difficulty must be between 0 and 5.", code='invalid_format')
#         return difficulty


class IgdbSearchSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class IgdbContainerSerializer(serializers.Serializer):
    data = IgdbSearchSerializer(many=True)
