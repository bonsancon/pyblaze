from pyblaze import BlazeClient
from requests import RequestException


class GameClient(BlazeClient):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def current(self):
        response = self._send_request(
            'GET',
            f'{self._url_api}/{self._game_namespace}/current',
        )

        if response.status_code != 200:
            raise RequestException(
                f'[{self._game_namespace} - current] Error code {response.status_code}',
            )

        return self._config['responses']['current'](**response.json())

    def get_game_by_id(self, game_id: str, page: int = None):
        # Page parameter only works in Double game
        page_text = ''
        if page is not None:
            page_text = f'?page={page}'

        response = self._send_request(
            'GET',
            f'{self._url_api}/{self._game_namespace}/{game_id}{page_text}',
        )

        if response.status_code != 200:
            raise RequestException(
                f'[{self._game_namespace} - get_game_by_id] Error code {response.status_code}',
            )

        return self._config['responses']['get_game_by_id'](**response.json())

    def recent(self):
        response = self._send_request(
            'GET',
            f'{self._url_api}/{self._game_namespace}/recent',
        )

        if response.status_code != 200:
            raise RequestException(
                f'[{self._game_namespace} - recent] Error code {response.status_code}',
            )

        return self._config['responses']['recent'](data=response.json())

    def recent_history(self):
        response = self._send_request(
            'GET',
            f'{self._url_api}/{self._game_namespace}/recent/history',
        )

        if response.status_code != 200:
            raise RequestException(
                f'[{self._game_namespace} - recent_history] Error code {response.status_code}',
            )

        return self._config['responses']['recent_history'](**response.json())
