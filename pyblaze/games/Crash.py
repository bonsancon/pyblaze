from pyblaze.enums import Game
from pyblaze.games import GameClient
from pyblaze.mixins import Hashable
from pyblaze.models.crash import CurrentResponse, \
    GetGameByIdResponse, \
    RecentHistoryResponse, \
    RecentsResponse, \
    Result


class Crash(GameClient, Hashable):
    # The hash of bitcoin block 570128
    # (https://medium.com/@blazedev/blaze-com-crash-seeding-event-v2-d774d7aeeaad)
    CLIENT_SEED = '0000000000000000000415ebb64b0d51ccee0bb55826e43846e5bea777d91966'
    FINAL_SEED = '492bd10144a3525e2745718fe4d25e08affbea483872d8e8b86191b20ce0a7a8'

    # Use the most significant 52 - bit from the hash to calculate the crash point
    MOST_SIGNIFICANT_BIT = 2 ** 52

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._game_namespace = Game.CRASH.value
        self._config = {
            'responses': {
                'current': CurrentResponse,
                'get_game_by_id': GetGameByIdResponse,
                'recent_history': RecentHistoryResponse,
                'recent': RecentsResponse,
            },
        }

    def _get_result_by_hexadecimal(self, hexadecimal_digits: str) -> Result:
        if int(hexadecimal_digits, 16) % 33 == 0:
            return Result(crash_point=1)

        hexadecimal_digits = int(hexadecimal_digits[:13], 16)
        crash_point = ((100 * self.MOST_SIGNIFICANT_BIT - hexadecimal_digits) /
                       (self.MOST_SIGNIFICANT_BIT - hexadecimal_digits)) // 1

        return Result(crash_point=(crash_point / 100.0))
