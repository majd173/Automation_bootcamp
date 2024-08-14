import logging
import requests
from api_automation_projects.pet_store.infra.api_wrapper import ApiWrapper
from api_automation_projects.pet_store.infra.config_provider import ConfigProvider
from api_automation_projects.pet_store.logic.entity.user_details import UserDetails
from api_automation_projects.pet_store.pet_store_data_base.users_data_base import UserDataBase


class UserPage:
    # This class manages the user page of the website and it's functionalities.

    USER_NAME = "user/login?username="
    USE_PASSWORD = "&password="
    USER_LOGOUT = "user/logout"
    USER_CREATE = "user/createWithList"
    USER_GET = "user/"

    def __init__(self, request: ApiWrapper):
        try:
            self._request = request
            self._api = ApiWrapper()
            self._config = ConfigProvider().load_from_file(
                r"/api_automated_testing\pet_store\pet_store.json")
            self._url = self._config['base_url']
            self._user_database = UserDataBase(self._config['user_database'])
            self._user_database.create_connection()
            self._user_database.create_table(self._config['users_table'])
        except ImportError:
            logging.error(f'Import error: {ImportError}')

    # --------------------------------------------------------------------------------------
    # GET REQUEST
    # This function receives a get request of the login process by
    # a user's name and password.

    def login_user(self, name, password):
        try:
            logging.info("Sending get request to the server.")
            return self._request.get_request(
                f'{self._url}{self.USER_NAME}'
                f'{name}{self.USE_PASSWORD}{password}')
        except requests.RequestException as e:
            logging.error(f'Get request has not been sent.: {e}')

    # --------------------------------------------------------------------------------------
    # GET REQUEST
    # This function receives a get request of the logout process by

    def user_logout(self):
        try:
            logging.info("Sending get request to the server.")
            return self._request.get_request(
                f'{self._url}{self.USER_LOGOUT}')
        except requests.RequestException as e:
            logging.error(f'Get request has not been sent.: {e}')

    # --------------------------------------------------------------------------------------
    # POST REQUEST
    # This function adds new user to the users list.
    def create_users_list(self, user: UserDetails):
        try:
            logging.info("Sending post request.")
            response = self._request.post_request(
                f'{self._config['base_url']}{self.USER_CREATE}',
                [user.to_dict()])
            self._user_database.execute_query(self._config['user_insertion'],
                                        (user.user_id, user.username, user.firstname, user.lastname, user.user_status))
            self._user_database.execute_query("DELETE FROM users")
            self._user_database.close_connection()
            return response
        except requests.RequestException as e:
            logging.error(f'Post request has not been sent.: {e}')

    # --------------------------------------------------------------------------------------
    # GET REQUEST
    # This functions receives a response of getting a username by its username.
    def get_user_by_username(self, username):
        try:
            logging.info("Sending get request to the server.")
            return self._request.get_request(
                f'{self._config['base_url']}{self.USER_GET}{username}')
        except requests.RequestException as e:
            logging.error(f'Get request has not been sent.: {e}')

    # --------------------------------------------------------------------------------------
