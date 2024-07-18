import json
import logging

import requests

from API_Project.pet_store.infra.API_Wrapper import APIWrapper
from API_Project.pet_store.infra.config_provider import ConfigProvider
from API_Project.deck_of_cards.infra.logger_setup import LoggingSetup


class PetStoreWeb:

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
    def pet_by_status(self, status):
        try:
            return self._request.get_request(
                f'{self._url}/v2/pet/findByStatus?status={status}')
        except Exception as e:
            logging.error(f'Can not get a request: {e}')

    def pet_by_status_get_json(self, key, status):
        try:
            logging.info("Sending JSON request to the server.")
            json_file = self._request.get_request(
                f'{self._url}/v2/pet/findByStatus?status={status}').json()
            if json_file:
                logging.info("JSON request has been obtained.")
                value = json_file[key]
                return value
            logging.error("JSON request has not been obtained.")
        except requests.RequestException as e:
            logging.error(f'Cannot get a request: {e}')

    # --------------------------------------------------------------------------------------
    # GET REQUEST

    def store_inventory(self):
        try:
            return self._request.get_request(f'{self._url}/v2/store/inventory')
        except Exception as e:
            logging.error(f'Can not get a request: {e}')

    def store_inventory_get_json(self, key):
        try:
            logging.info("Sending JSON request to the server.")
            json_file = self.store_inventory().json()
            if json_file:
                logging.info("JSON request has been obtained.")
                value = json_file[key]
                return value
            logging.error("JSON request has not been obtained.")
        except requests.RequestException as e:
            logging.error(f'Cannot get a request: {e}')

    # --------------------------------------------------------------------------------------
    def store_order(self):
        try:
            return self._request.post_request(f'{self._url}/v2/store/order')
        except requests.RequestException as e:
            logging.error(f'Cannot get a request: {e}')

    # POST REQUEST
    def store_order_add(self, new_body):
        # new_body_to_json = json.dumps(new_body)
        post = self._request.post_request(f'{self._url}/v2/store/order', new_body)
        logging.info(f'Posted body:\n{new_body}')
        return post

    # --------------------------------------------------------------------------------------
    # GET REQUEST

    def store_order_by_id(self, i, key):
        try:
            logging.info("Sending JSON request to the server.")
            json_file = self._request.get_request(f'{self._url}/v2/store/order/{i}').json()
            if json_file:
                logging.info("JSON request has been obtained.")
                value = json_file[key]
                return value
            logging.error("JSON request has not been obtained.")
        except Exception as e:
            logging.error(f'Can not get a request: {e}')

    # --------------------------------------------------------------------------------------
    # GET REQUEST

    def username_get_by_key_value_1(self, value):
        response = self._request.get_request(f'{self._url}/v2/user/{value}')
        return response
    def username_get_by_key_value_2(self, key, value):
        try:
            logging.info("Sending JSON request to the server.")
            json_file = self._request.get_request(f'{self._url}/v2/user/{value}').json()
            if json_file:
                logging.info("JSON request has been obtained.")
                result = json_file[key]
                return result
            logging.error("JSON request has not been obtained.")
        except Exception as e:
            logging.error(f'Can not get a request: {e}')
    # --------------------------------------------------------------------------------------
    # GET REQUEST
    def login_user(self, name, password, key):
        try:
            logging.info("Sending JSON request to the server.")
            json_file = self._request.get_request(
                f'{self._url}/v2/user/{name}'
                f' /v2/user/login?username={name}&password={password}').json()
            if json_file:
                logging.info("JSON request has been obtained.")
                value = json_file[key]
                logging.info(f"Value for key '{key}': {value}")
                return value
            logging.error("JSON request has not been obtained.")
        except requests.RequestException as e:
            logging.error(f'Cannot get a request: {e}')