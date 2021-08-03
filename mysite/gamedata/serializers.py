from rest_framework import serializers
from .models import GameInfo, IgdbLink, GameSubmissions


class GameInfoSerializer(serializers.ModelSerializer):

    igdb_id = serializers.ReadOnlyField(source='igdblink.igdb_id')

    class Meta:
        model = GameInfo
        fields = [
            'id',
            'name',
            'time',
            'difficulty',
            'igdb_id'
        ]


class GameInfoContainerSerializer(serializers.Serializer):
    data = GameInfoSerializer(many=True)


class GameSubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameSubmissions
        fields = [
            'game',
            'time',
            'difficulty'
        ]


class IgdbSearchSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()



class IgdbContainerSerializer(serializers.Serializer):
    data = IgdbSearchSerializer(many=True)

