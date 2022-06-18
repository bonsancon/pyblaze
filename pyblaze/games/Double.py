from pyblaze.enums import Game
from pyblaze.games import GameClient


class Double(GameClient):
    _game_namespace = Game.DOUBLE.value
