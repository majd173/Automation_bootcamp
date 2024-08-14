import requests
from api_automation_testing.pet_store.infra.response_wrapper import ResponseWrapper



class ApiWrapper:
    """
    This class manages types of requests can be used in logic classes.
    """

    def __init__(self):
        self._request = None

    def get_request(self, url, headers=None, body=None):
        response = requests.get(url, headers=headers, json=body)
        return ResponseWrapper(response.ok, response.status_code, response.json())

    def post_request(self, url, body=None):
        respnse = requests.post(url, json=body)
        return ResponseWrapper(respnse.ok, respnse.status_code, respnse.json())

    def delete_request(self, url, headers=None, body=None):
        if headers is None:
            headers = {}
        # Ensure all header values are strings.
        headers = {k: str(v) for k, v in headers.items()}
        return requests.delete(url, headers=headers, json=body)
