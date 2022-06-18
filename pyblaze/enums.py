from enum import Enum


class Game(Enum):
    CRASH = 'crash_games'
    DOUBLE = 'roulette_games'


class DoubleColor(Enum):
    WHITE = 'white'  # 0
    RED = 'red'  # 1
    BLACK = 'black'  # 2

    @staticmethod
    def create_by_int(color_int: int) -> 'DoubleColor':
        if color_int == 1:
            return DoubleColor.RED
        if color_int == 2:
            return DoubleColor.BLACK

        return DoubleColor.WHITE
