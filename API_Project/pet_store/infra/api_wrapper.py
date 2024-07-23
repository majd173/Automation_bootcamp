import requests
from API_Project.pet_store.infra.response_wrapper import ResponseWrapper





class ApiWrapper:

    """
    This class manages types of requests can be used in logic classes.
    """
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

    # @staticmethod
    # def get_request(url, headers=None, body=None):
    #     response = requests.get(url, headers=headers, json=body)
    #     return ResponseWrapper(response.ok, response.status_code, response.json())
    #
    # @staticmethod
    # def post_request(url, headers=None, body=None):
    #     response = requests.post(url, headers=headers, json=body)
    #     return ResponseWrapper(response.ok, response.status_code, response.json())
    #
    #

