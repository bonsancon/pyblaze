import requests


class BlazeClient:
    URL_API_V1 = 'https://blaze.com/api'
    URL_API_V2 = 'https://api-v2.blaze.com'

    def __init__(self, version: int = 1):
        self._session = requests.Session()
        # See https://fake-useragent.herokuapp.com/browsers/0.1.11
        # self._user_agent = UserAgent(
        #     cache=False,
        # )
        self._set_version(version)

    def _set_version(self, version: int) -> None:
        self._url_api = self.URL_API_V1

        if version == 2:
            self._url_api = self.URL_API_V2

    def _send_request(self, method, url, **kwargs):
        kwargs['headers'] = {
            # 'User-Agent': self._user_agent.random,
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/41.0.2228.0 Safari/537.36',
        }
        response = self._session.request(method, url, **kwargs)

        if response.status_code == 200:
            return response.json()

        return response

    def announcement(self):
        data = self._send_request(
            'GET',
            f'{self._url_api}/announcement',
        )

        return data

    def chat_rooms(self):
        data = self._send_request(
            'GET',
            f'{self._url_api}/chat_rooms',
        )

        return data

    def chat_room(self, chat_number: int = 2):
        data = self._send_request(
            'GET',
            f'{self._url_api}/chat_rooms/{chat_number}',
        )

        return data

    def country(self):
        data = self._send_request(
            'GET',
            f'{self._url_api}/country',
        )

        return data

    def currencies(self):
        data = self._send_request(
            'GET',
            f'{self._url_api}/currencies',
        )

        return data

    def version(self):
        data = self._send_request(
            'GET',
            f'{self._url_api}/version',
        )

        return data

    def settings(self):
        data = self._send_request(
            'GET',
            f'{self._url_api}/settings',
        )

        return data

    def time(self):
        data = self._send_request(
            'GET',
            f'{self._url_api}/time',
        )

        return data
