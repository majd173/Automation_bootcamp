import requests
from api.deck_of_cards.infra.logger_setup import LoggingSetup

class APIWrapper:

    def __init__(self):
        self._request = None

    def get_request(self, url, body=None):
        return requests.get(url, json=body)

    def post_request(self, url, body=None):
        return requests.post(url, json=body)

    def delete_request(self, url, data=None):
        return requests.delete(url, json=data)

