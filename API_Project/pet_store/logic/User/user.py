import logging
import requests
from API_Project.pet_store.infra.API_Wrapper import APIWrapper
from API_Project.pet_store.infra.config_provider import ConfigProvider


class UserPage:
    # This class manages the user page of the website and it's functionalities.

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
    # This function receives a get request of the username by its name.

    def username_get_by_key_value_check_st_ok(self, name):
        try:
            logging.info("Sending get request to the server.")
            response = self._request.get_request(f'{self._url}/v2/user/{name}')
            if response:
                logging.info("Response has been received.")
                return response
            else:
                logging.error("Response has not been received.")
        except requests.RequestException as e:
            logging.error(f'Cannot send a request: {e}')

    # This function receives a JSON file of a username buy its name and
    # returns a value by a specific key.

    def username_get_by_key_value(self, key, name):
        try:
            logging.info("Sending JSON request to the server.")
            json_file = self._request.get_request(
                f'{self._url}/v2/user/{name}').json()
            if json_file:
                logging.info("JSON response has been received.")
                value = json_file[key]
                return value
            logging.error("JSON response has not been received.")
        except Exception as e:
            logging.error(f'Can not get a request: {e}')

    # --------------------------------------------------------------------------------------
    # GET REQUEST
    # This function receives a get request of the login process by
    # a user's name and password.

    def login_user_check_st_ok(self, name, password):
        try:
            logging.info("Sending get request to the server.")
            response = self._request.get_request(
                f'{self._url}/v2/user/login?username={name}&password={password}')
            if response:
                logging.info("Response has been received.")
                return response
            else:
                logging.error("Response has not been received.")
        except requests.RequestException as e:
            logging.error(f'Cannot send a request: {e}')

    # This function receives a JSON file for a login by name and password
    # and returns a value by a specific key.

    def login_user(self, name, password, key):
        try:
            logging.info("Sending JSON request to the server.")
            json_file = self._request.get_request(
                f'{self._url}/v2/user/login?username={name}&password={password}').json()
            if json_file:
                logging.info("JSON response has been received.")
                value = json_file[key]
                return value
            logging.error("JSON response has not been received.")
        except requests.RequestException as e:
            logging.error(f'Cannot send a request: {e}')

    # --------------------------------------------------------------------------------------
    # GET REQUEST
    # This function receives a get request of the logout process by

    def user_logout_check_st_ok(self):
        try:
            logging.info("Sending get request to the server.")
            response = self._request.get_request(
                f'{self._url}/v2/user/logout')
            if response:
                logging.info("Response has been received.")
                return response
            logging.error("Response has not been received.")
        except requests.RequestException as e:
            logging.error(f'Cannot send a request: {e}')

    # This function receives a JSON file for a logout by name and password

    def user_logout_message(self, key):
        try:
            logging.info("Sending JSON request.")
            json_file = self._request.get_request(
                f'{self._url}/v2/user/logout').json()
            if json_file:
                logging.info("JSON response has been received.")
                value = json_file[key]
                return value
            logging.error("JSON response has not been received.")
        except requests.RequestException as e:
            logging.error(f'Cannot send a request: {e}')


    # This function adds new user to the users list.
    def create_users_list(self, new_body):
        logging.info("Sending post request.")
        response = self._request.post_request(
            f'{self._config['base_url']}/v2/user/createWithList', new_body)
        if response:
            logging.info("Post request has been sent.")
            return response
        logging.error("Post request has not been sent.")
