import logging
import requests
from API_Project.pet_store.infra.API_Wrapper import APIWrapper
from API_Project.pet_store.infra.config_provider import ConfigProvider


class UserPage:

    def __init__(self, request: APIWrapper):
        try:
            self._request = request
            self._api = APIWrapper()
            self._config = ConfigProvider().load_from_file("../pet_store.json")
            self._url = self._config['base_url']
        except ImportError:
            logging.error("Can not open pet_store.json file.")

# --------------------------------------------------------------------------------------

    # GET REQUEST
    def username_get_by_key_value(self, key, name):
        try:
            logging.info("Sending get request to the server.")
            response = self._request.get_request(f'{self._url}/v2/user/{name}')
            logging.info(f'Response status code: {response.status_code}')
            logging.info(f'Response is ok: {response.ok}')
            logging.info("Sending JSON request to the server.")
            json_file = response.json()
            if json_file:
                logging.info("JSON request has been received.")
                print(json_file)
                value = json_file[key]
                return value
            logging.error("JSON request has not been obtained.")
        except Exception as e:
            logging.error(f'Can not get a request: {e}')
    # --------------------------------------------------------------------------------------
    # GET REQUEST
    def login_user(self, name, password, key):
        try:
            logging.info("Sending get request to the server.")
            response = self._request.get_request(
                f'{self._url}/v2/user/login?username={name}&password={password}')
            logging.info(f'Response status code: {response.status_code}')
            logging.info(f'Response is ok: {response.ok}')
            logging.info("Sending JSON request to the server.")
            json_file = response.json()
            if json_file:
                logging.info("JSON request has been received.")
                print(json_file)
                value = json_file[key]
                return value
            logging.error("JSON request has not been received.")
        except requests.RequestException as e:
            logging.error(f'Cannot send a request: {e}')

    # --------------------------------------------------------------------------------------
    # DELETE REQUEST

    def delete_user_by_name(self, name):
        try:
            logging.info("Sending delete request to the server.")
            response = self._request.delete_request(
                f'{self._config}/v2/user/{name}')
            if response:
                logging.info("Delete request has been received.")
                return response
            logging.error("Delete request has not been received.")
        except requests.RequestException as e:
            logging.error(f'Cannot send a request: {e}')