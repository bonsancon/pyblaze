from pyblaze.enums import Game
from pyblaze.games import GameClient
from pyblaze.models.double import CurrentResponse, RecentsResponse


class Double(GameClient):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._game_namespace = Game.DOUBLE.value
        self._config = {
            'responses': {
                'current': CurrentResponse,
                'recents': RecentsResponse,
            },
        }
