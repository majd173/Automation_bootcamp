import logging
import requests
from API_Project.pet_store.infra.api_wrapper import ApiWrapper
from API_Project.pet_store.infra.config_provider import ConfigProvider
from API_Project.pet_store.logic.entity.pet_details import PetDetails


class PetPage:
    # This class manages the pet's page and functionalities.

    PET_BY_STATUS = "pet/findByStatus?status="
    ADD_PET = "pet"
    PET_BY_ID = "pet/"




    def __init__(self, request: ApiWrapper):
        try:
            self._request = request
            self._api = ApiWrapper()
            self._config = ConfigProvider().load_from_file("../pet_store.json")
            self._url = self._config['base_url']
        except ImportError:
            logging.error("Can not open pet_store.json file.")


    # --------------------------------------------------------------------------------------
    # GET REQUEST
    # This functions receives a response of a pet by its status.
    def pet_by_status(self, status):
        try:
            logging.info("Sending get request to the server.")
            return self._request.get_request(
                f'{self._url}{self.PET_BY_STATUS}{status}')
        except requests.RequestException as e:
            logging.error(f'Get request has not been sent.: {e}')

    # --------------------------------------------------------------------------------------
    # POST REQUEST
    # This function post a request includes new pet details to be added.
    def add_pet(self, pet: PetDetails):
        try:
            logging.info("Sending post request to the server.")
            return self._request.post_request(
                f'{self._config['base_url']}{self.ADD_PET}', pet.to_dic())
        except requests.RequestException as e:
            logging.error("Post response has not been sent.")

    def get_pet_by_id(self, id):
        try:
            logging.info("Sending get request to the server.")
            return self._request.get_request(
                f'{self._url}{self.PET_BY_ID}{id}')
        except requests.RequestException as e:
            logging.error(f'Get request has not been sent.: {e}')

    # --------------------------------------------------------------------------------------
