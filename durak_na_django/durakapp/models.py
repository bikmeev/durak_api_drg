from django.db import models

from django.db import models

class Lobby(models.Model):
    lobby_uuid = models.UUIDField(primary_key=True)
    player1 = models.UUIDField()
    player2 = models.UUIDField(blank=True, null=True)
    is_game_started = models.BooleanField(default=False)

class Game(models.Model):
    lobby = models.OneToOneField(Lobby, on_delete=models.CASCADE)
    # Дополнительные поля игры

class Player(models.Model):
    player_uuid = models.UUIDField(primary_key=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    # Дополнительные поля игрока

