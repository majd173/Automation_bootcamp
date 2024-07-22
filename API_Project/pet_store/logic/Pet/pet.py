import logging
import requests
from API_Project.pet_store.infra.API_Wrapper import APIWrapper
from API_Project.pet_store.infra.config_provider import ConfigProvider
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
                f'{self._url}{self._config['pet_by_status']}{status}')
            if response:
                logging.info("Get response has been received.")
                return response
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
            f'{self._config['base_url']}{self._config['add_pet']}', pet.to_dic())
        if response:
            logging.info("Post response has been received.")
            return response
        logging.error("Post response has not been received.")

    def get_pet_by_id(self, id):
        try:
            logging.info("Sending get request to the server.")
            response = self._request.get_request(
                f'{self._url}{self._config['pet_by_id']}{id}')
            if response:
                logging.info("Get response has been received.")
                return response
            else:
                logging.error("Get response has not been received.")
        except requests.RequestException as e:
            logging.error(f'Get request has not been sent.: {e}')

    # --------------------------------------------------------------------------------------
    # DELETE REQUEST
    # This function receives a delete request after sending a post one.
    # it verifies the deleting process.

    def delete_pet(self, pet: PetDetails, id):
        try:
            logging.info("Sending post request to the server.")
            response = self._request.post_request(
                f'{self._config['base_url']}{self._config['add_pet']}', pet.to_dic())
            if response:
                logging.info("Post response has been received.")
            else:
                logging.error("Post response has not been received.")
            logging.info("Sending delete request to the server.")
            delete = self._request.delete_request(f'{self._url}{self._config['pet_by_id']}{id}{self.DELETE_PET_HEADER}')
            if delete:
                logging.info("Delete response has been received.")
                json_file = delete.json()
                return json_file
            else:
                logging.error("Delete response has not been received.")
        except requests.RequestException as e:
            logging.error(f'Post request has not been sent.: {e}')




