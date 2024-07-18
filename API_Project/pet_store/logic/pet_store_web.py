import json
import logging
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
    def pet_by_status_available(self):
        try:
            return self._request.get_request(
                f'{self._url}/v2/pet/findByStatus?status=available')
        except Exception:
            logging.error("Can not get a request.")

    def pet_by_status_available_get_json(self, key):
        try:
            json = self.pet_by_status_available().json()
            if json:
                logging.info("json request was got.")
                return json[key]
            logging.error("Can not get a json request.")
        except Exception:
            logging.error("Can not get a json request.")

    # --------------------------------------------------------------------------------------
    # GET REQUEST

    def store_inventory(self):
        try:
            return self._request.get_request(f'{self._url}/v2/store/inventory')
        except Exception:
            logging.error("Can not get a request.")

    def store_inventory_get_json(self, key):
        try:
            json = self.store_inventory().json()
            if json:
                logging.info("json request was got.")
                return json[key]
            logging.error("Can not get a json request.")
        except Exception:
            logging.error("Can not get a json request.")

    # --------------------------------------------------------------------------------------
    def store_order(self):
        try:
            return self._request.post_request(f'{self._url}/v2/store/order')
        except Exception:
            logging.error("Can not get a request.")

    # POST REQUEST
    def store_order_add(self, new_body):
        new_body_to_json = json.dumps(new_body)
        post = self._request.post_request(f'{self._url}/v2/store/order', new_body_to_json)
        logging.info(f'Posted body:\n{new_body_to_json}')
        return post

    # --------------------------------------------------------------------------------------
    # GET REQUEST

    def store_order_by_id(self, i):
        try:
            request_json = self._request.get_request(f'{self._url}/v2/store/order/{i}').json()
            id_value = request_json['id']
            return id_value
        except Exception as e:
            logging.error(f'Can not get a request: {e}')
