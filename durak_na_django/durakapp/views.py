from django.shortcuts import render

from rest_framework import generics
from .models import Lobby, Game, Player
from .serializers import LobbySerializer, GameSerializer, PlayerSerializer

class LobbyCreateView(generics.CreateAPIView):
    queryset = Lobby.objects.all()
    serializer_class = LobbySerializer

class LobbyEnterView(generics.UpdateAPIView):
    queryset = Lobby.objects.all()
    serializer_class = LobbySerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.player2:
            instance.player2 = request.data.get('player_uuid')
            instance.is_game_started = True
            instance.save()
            # Отправить уведомление о входе в лобби в чат с ботом
            return self.partial_update(request, *args, **kwargs)
        else:
            # Вернуть сообщение, что лобби заполнено
            pass

class GameView(generics.RetrieveUpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Логика обработки ходов и проверок игры
        return self.retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        # Логика обновления состояния игры
        return self.update(request, *args, **kwargs)

class PlayerBalanceView(generics.UpdateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'player_uuid'
    lookup_url_kwarg = 'player_uuid'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        # Логика обновления баланса игрока
        return self.update(request, *args, **kwargs)
