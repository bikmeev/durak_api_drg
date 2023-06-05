from django.urls import path
from .views import LobbyCreateView, LobbyEnterView, GameView, PlayerBalanceView

urlpatterns = [
    path('lobby/create/', LobbyCreateView.as_view(), name='lobby-create'),
    path('lobby/enter/', LobbyEnterView.as_view(), name='lobby-enter'),
    path('game/', GameView.as_view(), name='game'),
    path('player/<uuid:player_uuid>/balance/', PlayerBalanceView.as_view(), name='player-balance'),
]
