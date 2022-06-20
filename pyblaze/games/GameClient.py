from pyblaze import BlazeClient
from requests import RequestException


class GameClient(BlazeClient):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def recent(self):
        response = self._send_request(
            'GET',
            f'{self._url_api}/{self._game_namespace}/recent',
        )

        if response.status_code != 200:
            raise RequestException(
                f'[{self._game_namespace} - recents] Error code {response.status_code}',
            )

        return self._config['responses']['recents'](data=response.json())

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
