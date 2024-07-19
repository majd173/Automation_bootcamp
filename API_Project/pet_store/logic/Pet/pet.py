import logging
import requests
from API_Project.pet_store.infra.API_Wrapper import APIWrapper
from API_Project.pet_store.infra.config_provider import ConfigProvider


class PetPage:

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

    def pet_by_status_get_json(self, key, endpoint):
        try:
            logging.info("Sending get request to the server.")
            response = self._request.get_request(
                f'{self._url}/v2/pet/findByStatus?status={endpoint}')
            logging.info(f'Response status code is: {response.status_code}')
            logging.info(f'Response is ok: {response.ok}')
            logging.info("Sending JSON request to the server.")
            json_file = response.json()
            if json_file:
                logging.info("JSON request has been received.")
                value = json_file[0][key]
                return value
            logging.error("JSON request has not been receiver.")
        except requests.RequestException as e:
            logging.error(f'Cannot send a request: {e}')

# --------------------------------------------------------------------------------------

    # POST REQUEST

    def add_pet(self, new_body):
        logging.info("Sending post request.")
        post = self._request.post_request(
            f'{self._config['base_url']}/v2/pet', new_body)
        if post:
            logging.info("Post request has been sent.")
            return post
        logging.error("Post request has not been sent.")