import logging
import requests
from API_Project.pet_store.infra.API_Wrapper import APIWrapper
from API_Project.pet_store.infra.config_provider import ConfigProvider


class StorePage:

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
    def store_inventory_check_st_ok(self):
        try:
            logging.info("Sending get request to the server.")
            response = self._request.get_request(
                f'{self._url}/v2/store/inventory')
            if response:
                logging.info("Response has been received.")
                return response
            else:
                logging.error("Response has not been received.")
        except requests.RequestException as e:
            logging.error(f'Cannot senf a request: {e}')


    def store_inventory(self, key):
        try:
            logging.info("Sending JSON request to the server.")
            json_file = self._request.get_request(
                f'{self._url}/v2/store/inventory').json()
            if json_file:
                logging.info("JSON response has been received.")
                value = json_file[key]
                return value
            logging.error("JSON response has not been received.")
        except requests.RequestException as e:
            logging.error(f'Cannot get a request: {e}')

    # --------------------------------------------------------------------------------------
    # POST REQUEST
    def store_order_add(self, new_body):
        logging.info("Sending post request.")
        post = self._request.post_request(
            f'{self._url}/v2/store/order', new_body)
        if post:
            logging.info("Post request has been sent.")
            return post
        logging.error("Post request has not been sent.")


    # --------------------------------------------------------------------------------------
    # GET REQUEST

    def store_order_by_id(self, endpoint, key):
        try:
            logging.info("Sending JSON request to the server.")
            json_file = self._request.get_request(
                f'{self._url}/v2/store/order/{endpoint}').json()
            if json_file:
                logging.info("JSON response has been received.")
                value = json_file[key]
                return value
            logging.error("JSON response has not been received.")
        except Exception as e:
            logging.error(f'Can not get a request: {e}')