import logging
import requests
from API_Project.pet_store.infra.API_Wrapper import APIWrapper
from API_Project.pet_store.infra.config_provider import ConfigProvider
from API_Project.pet_store.infra.response_wrapper import ResponseWrapper
from API_Project.pet_store.logic.entity.pet_details import PetDetails


class PetPage:
    # This class manages the pet's page and functionalities.



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
    # This functions receives a response of a pet by its status.
    def pet_by_status(self, status):
        try:
            logging.info("Sending get request to the server.")
            response = self._request.get_request(
                f'{self._url}pet/findByStatus?status={status}')
            if response:
                logging.info("Get response has been received.")
                return ResponseWrapper(ok=response.ok, status_code=response.status_code, data=response.json())
            else:
                logging.error("Get response has not been received.")
        except requests.RequestException as e:
            logging.error(f'Get request has not been sent.: {e}')

    # --------------------------------------------------------------------------------------
    # POST REQUEST
    # This function post a request includes new pet details to be added.
    def add_pet(self, pet: PetDetails):
        logging.info("Sending post request to the server.")
        response = self._request.post_request(
            f'{self._config['base_url']}pet', pet.to_dic())
        if response:
            logging.info("Post response has been received.")
            return ResponseWrapper(ok=response.ok, status_code=response.status_code, data=response.json())
        logging.error("Post response has not been received.")

    def get_pet_by_id(self, id):
        try:
            logging.info("Sending get request to the server.")
            response = self._request.get_request(
                f'{self._url}pet/{id}')
            if response:
                logging.info("Get response has been received.")
                return ResponseWrapper(ok=response.ok, status_code=response.status_code, data=response.json())
            else:
                logging.error("Get response has not been received.")
        except requests.RequestException as e:
            logging.error(f'Get request has not been sent.: {e}')

    # --------------------------------------------------------------------------------------
