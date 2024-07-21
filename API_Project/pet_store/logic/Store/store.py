import logging
import requests
from API_Project.pet_store.infra.API_Wrapper import APIWrapper
from API_Project.pet_store.infra.config_provider import ConfigProvider
from API_Project.pet_store.logic.entity.order_details import OrderDetails


class StorePage:
    # This class manages store page of the website and it's functionalities.


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
    # This function receives a get request of the inventory of the store.
    def store_inventory(self):
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


    # --------------------------------------------------------------------------------------
    # POST REQUEST
    # This function post a request includes new order details to be added.
    def store_order_add(self, order: OrderDetails):
        logging.info("Sending post request.")
        post = self._request.post_request(
            f'{self._url}/v2/store/order', order.to_dict())
        if post:
            logging.info("Post request has been sent.")
            return post
        logging.error("Post request has not been sent.")


    # --------------------------------------------------------------------------------------
    # GET REQUEST
    # This function receives a JSON file of an order by its endpoint
    # and return a value by a specific key.

    def store_order_by_id(self, id):
        try:
            logging.info("Sending get request to the server.")
            response = self._request.get_request(
                f'{self._url}/v2/store/order/{id}')
            if response:
                logging.info("Get response has been received.")
                return response
            logging.error("Get response has not been received.")
        except Exception as e:
            logging.error(f'Can not send a request: {e}')