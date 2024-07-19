import requests
from API_Project.pet_store.infra.logger_setup import LoggingSetup

class APIWrapper:

    def __init__(self):
        self._request = None

    def get_request(self, url, headers=None, body=None):
        return requests.get(url, headers=headers, json=body)

    def post_request(self, url, body=None):
        return requests.post(url, json=body)

    def delete_request(self, url, headers=None, data=None):
        if headers is None:
            headers = {}
        # Ensure all header values are strings
        headers = {k: str(v) for k, v in headers.items()}
        return requests.delete(url, headers=headers, json=data)




