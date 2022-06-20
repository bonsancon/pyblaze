from pyblaze.enums import DoubleColor, Game
from pyblaze.games import GameClient
from pyblaze.mixins import Hashable
from pyblaze.models.double import CurrentResponse, \
    GetGameByIdResponse, \
    RecentsResponse, \
    Result


class Double(GameClient, Hashable):
    # The hash of bitcoin block 570120
    # (https://medium.com/@blazedev/blaze-com-double-seeding-event-d3290ef13454)
    CLIENT_SEED = '0000000000000000002aeb06364afc13b3c4d52767e8c91db8cdb39d8f71e8dd'
    FINAL_SEED = '99384f03b5f52758f8c6037adca8d27d7d940dfe3cf15bbb763399bea0bbf914'

    DOUBLE_DIV = 15

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._game_namespace = Game.DOUBLE.value
        self._config = {
            'responses': {
                'current': CurrentResponse,
                'recent': RecentsResponse,
                'get_game_by_id': GetGameByIdResponse,
            },
        }

    def _get_result_by_hexadecimal(self, hexadecimal_digits: str) -> Result:
        modulo = int(hexadecimal_digits, 16) % self.DOUBLE_DIV

        if modulo == 0:
            return Result(
                color=DoubleColor.WHITE.value,
                roll=modulo,
            )

        if modulo <= 7:
            return Result(
                color=DoubleColor.RED.value,
                roll=modulo,
            )

        return Result(
            color=DoubleColor.BLACK.value,
            roll=modulo,
        )
