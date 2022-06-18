from pyblaze.enums import Game
from pyblaze.games import GameClient


class Crash(GameClient):
    _game_namespace = Game.CRASH.value
