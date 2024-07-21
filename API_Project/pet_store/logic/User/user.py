import logging
import requests
from API_Project.pet_store.infra.API_Wrapper import APIWrapper
from API_Project.pet_store.infra.config_provider import ConfigProvider
from API_Project.pet_store.logic.entity.user_details import UserDetails


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
    # This function receives a get request of the login process by
    # a user's name and password.

    def login_user(self, name, password):
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

    # --------------------------------------------------------------------------------------
    # GET REQUEST
    # This function receives a get request of the logout process by

    def user_logout(self):
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

    # --------------------------------------------------------------------------------------
    # POST REQUEST
    # This function adds new user to the users list.
    def create_users_list(self, user: UserDetails):
        logging.info("Sending post request.")
        response = self._request.post_request(
            f'{self._config['base_url']}/v2/user/createWithList', [user.to_dict()])
        if response:
            logging.info("Post request has been sent.")
            return response
        logging.error("Post request has not been sent.")


    # --------------------------------------------------------------------------------------
    # GET REQUEST
    # This functions receives a response of getting a username by its username.
    def get_user_by_username(self, username):
        try:
            logging.info("Sending get request to the server.")
            response = self._request.get_request(
                f'{self._config['base_url']}/v2/user/{username}')
            if response:
                logging.info("Response has been received.")
                return response
            logging.error("Response has not been received.")
        except requests.RequestException as e:
            logging.error(f'Cannot send a request: {e}')

    # --------------------------------------------------------------------------------------


