from pyblaze.enums import Game
from pyblaze.games import GameClient
from pyblaze.models.crash import CurrentResponse, RecentsResponse


class Crash(GameClient):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._game_namespace = Game.CRASH.value
        self._config = {
            'responses': {
                'current': CurrentResponse,
                'recents': RecentsResponse,
            },
        }
