from rest_framework import serializers
from .models import Lobby, Game, Player

class LobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lobby
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
