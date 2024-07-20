import logging
import requests
from API_Project.pet_store.infra.API_Wrapper import APIWrapper
from API_Project.pet_store.infra.config_provider import ConfigProvider


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
    def pet_by_status_check_st_ok(self, endpoint):
        try:
            logging.info("Sending get request to the server.")
            response = self._request.get_request(
                f'{self._url}/v2/pet/findByStatus?status={endpoint}')
            if response:
                logging.info("Response has been received.")
                return response
            else:
                logging.error("Response has not been received.")
        except requests.RequestException as e:
            logging.error(f'Cannot senf a request: {e}')


    # This function receives a JSON file of a pet by its status
    # and returns a value by a specific key.
    def pet_by_status_get_json(self, key, endpoint):
        try:
            logging.info("Sending JSON request to the server.")
            json_file = self._request.get_request(
                f'{self._url}/v2/pet/findByStatus?status={endpoint}').json()
            if json_file:
                logging.info("JSON response has been received.")
                value = json_file[0][key]
                return value
            logging.error("JSON response has not been received.")
        except requests.RequestException as e:
            logging.error(f'Cannot send a request: {e}')

    # --------------------------------------------------------------------------------------
    # POST REQUEST
    # This function post a request includes new pet details to be added.
    def add_pet(self, new_body):
        logging.info("Sending post request.")
        post = self._request.post_request(
            f'{self._config['base_url']}/v2/pet', new_body)
        if post:
            logging.info("Post request has been sent.")
            return post
        logging.error("Post request has not been sent.")

    # --------------------------------------------------------------------------------------
    # DELETE REQUEST
    # This function receives a delete request after sending a post one.
    # it verifies the deleting process.

    def delete_pet(self, new_body, key):
        logging.info("Sending post request.")
        post = self._request.post_request(
            f'{self._config['base_url']}/v2/pet', new_body)
        if post:
            logging.info("Post request has been sent.")
            body = post.json()
        else:
            logging.error("Post request has not been sent.")
            return
        delete = self._request.delete_request(f'{self._url}/v2/pet/1', new_body)
        if delete:
            logging.info("Delete request has been sent.")
            json_file = delete.json()
            if json_file != body:
                logging.info("Delete request completed successfully.")
                value = json_file[key]
                return value
            logging.error("Delete request response matches post request response.")
        else:
            logging.error("Delete request has not been sent.")



