from abc import ABC
import hashlib
import hmac
from typing import List


class Hashable(ABC):

    def _get_result_by_hexadecimal(self, hexadecimal_digits: str):
        raise NotImplementedError('You must implement the "_get_result_by_hexadecimal" method.')

    def get_previous_game_hash_by_hash(self, hash_code: str) -> str:
        sha = hashlib.sha256()
        sha.update(hash_code.encode('utf-8'))

        return sha.hexdigest()

    def get_previous_games_to_hash_by_hash(self, hash_code: str, hash_match: str = None) -> List:
        if hash_match is None:
            hash_match = self.CLIENT_SEED

        results = []
        match = False

        while not match:
            if hash_code == hash_match:
                match = True

            results.append(self.get_result_by_hash(hash_code))
            hash_code = self.get_previous_game_hash_by_hash(hash_code)

        return results

    def get_previous_n_games_by_hash(self, hash_code: str, number_of_games: int = 10) -> List:
        results = []

        for count in range(number_of_games):
            results.append(self.get_result_by_hash(hash_code))
            hash_code = self.get_previous_game_hash_by_hash(hash_code)

        return results

    def get_result_by_hash(self, game_hash: str):
        hmac_new = hmac.new(str.encode(game_hash), b'', hashlib.sha256)
        hmac_new.update(self.CLIENT_SEED.encode('utf-8'))
        hexadecimal_digits = hmac_new.hexdigest()
        result = self._get_result_by_hexadecimal(hexadecimal_digits)
        result.hash = game_hash

        return result
