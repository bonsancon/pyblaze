from pyblaze import BlazeClient


class GameClient(BlazeClient):

    def recents(self):
        data = self._send_request(
            'GET',
            f'{self._url_api}/{self._game_namespace}/recent',
        )

        return data

    def current(self):
        data = self._send_request(
            'GET',
            f'{self._url_api}/{self._game_namespace}/current',
        )

        return data
