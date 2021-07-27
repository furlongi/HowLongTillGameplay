from rest_framework import serializers
from .models import GameInfo


class GameInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameInfo
        fields = [
            'name',
            'time',
            'difficulty'
        ]


# class GameSubmissionSerializer():



class IgdbSearchSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class IgdbContainerSerializer(serializers.Serializer):
    data = IgdbSearchSerializer(many=True)

