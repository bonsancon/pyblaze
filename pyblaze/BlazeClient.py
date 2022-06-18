from pyblaze.models.blaze import Announcement, \
    ChatRoomResponse, \
    ChatRoomsResponse, \
    Country, \
    Currencies, \
    Settings, \
    Time, \
    Version
import requests
from requests import RequestException


class BlazeClient:
    URL_API_V1 = 'https://blaze.com/api'
    URL_API_V2 = 'https://api-v2.blaze.com'

    def __init__(self, version: int = 1):
        self._session = requests.Session()
        self._set_version(version)

    def _set_version(self, version: int) -> None:
        self._url_api = self.URL_API_V1

        if version == 2:
            self._url_api = self.URL_API_V2

    def basic_response_treatment(self, response):
        if response.status_code == 200:
            return response.json()

        return response

    def _send_request(self, method, url, **kwargs):
        kwargs['headers'] = {
            # See https://fake-useragent.herokuapp.com/browsers/0.1.11
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/41.0.2228.0 Safari/537.36',
        }
        return self._session.request(method, url, **kwargs)

    def announcement(self):
        response = self._send_request(
            'GET',
            f'{self._url_api}/announcement',
        )

        if response.status_code != 200:
            raise RequestException(
                f'[Blaze - announcement] Error code {response.status_code}',
            )

        return Announcement(**response.json())

    def chat_rooms(self):
        response = self._send_request(
            'GET',
            f'{self._url_api}/chat_rooms',
        )

        if response.status_code != 200:
            raise RequestException(
                f'[Blaze - chat_rooms] Error code {response.status_code}',
            )

        return ChatRoomsResponse(data=response.json())

    def chat_room(self, chat_number: int = 2):
        response = self._send_request(
            'GET',
            f'{self._url_api}/chat_rooms/{chat_number}',
        )

        if response.status_code != 200:
            raise RequestException(
                f'[Blaze - chat_room {chat_number}] Error code {response.status_code}',
            )

        return ChatRoomResponse(**response.json())

    def country(self):
        response = self._send_request(
            'GET',
            f'{self._url_api}/country',
        )

        if response.status_code != 200:
            raise RequestException(
                f'[Blaze - country] Error code {response.status_code}',
            )

        return Country(**response.json())

    def currencies(self):
        response = self._send_request(
            'GET',
            f'{self._url_api}/currencies',
        )

        if response.status_code != 200:
            raise RequestException(
                f'[Blaze - currencies] Error code {response.status_code}',
            )

        return Currencies(data=response.json())

    def settings(self):
        response = self._send_request(
            'GET',
            f'{self._url_api}/settings',
        )

        if response.status_code != 200:
            raise RequestException(
                f'[Blaze - settings] Error code {response.status_code}',
            )

        return Settings(**response.json())

    def time(self):
        response = self._send_request(
            'GET',
            f'{self._url_api}/time',
        )

        if response.status_code != 200:
            raise RequestException(
                f'[Blaze - time] Error code {response.status_code}',
            )

        return Time(**response.json())

    def version(self):
        response = self._send_request(
            'GET',
            f'{self._url_api}/version',
        )

        if response.status_code != 200:
            raise RequestException(
                f'[Blaze - version] Error code {response.status_code}',
            )

        return Version(**response.json())
