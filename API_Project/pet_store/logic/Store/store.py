import logging
import requests
from API_Project.pet_store.infra.api_wrapper import ApiWrapper
from API_Project.pet_store.infra.config_provider import ConfigProvider
from API_Project.pet_store.infra.response_wrapper import ResponseWrapper
from API_Project.pet_store.logic.entity.order_details import OrderDetails


class StorePage:
    # This class manages store page of the website and it's functionalities.

    STORE_INVENTORY = "store/inventory"
    ADD_ORDER = "store/order"
    ORDER_BY_ID = "store/order/"



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
    # This function receives a get request of the inventory of the store.
    def store_inventory(self):
        try:
            logging.info("Sending get request to the server.")
            return self._request.get_request(
                f'{self._url}{self.STORE_INVENTORY}')
        except requests.RequestException as e:
            logging.error(f'Get request has not been sent.: {e}')


    # --------------------------------------------------------------------------------------
    # POST REQUEST
    # This function post a request includes new order details to be added.
    def store_order_add(self, order: OrderDetails):
        try:
            logging.info("Sending post request to the server.")
            return self._request.post_request(
                f'{self._url}{self.ADD_ORDER}', order.to_dict())
        except requests.RequestException as e:
            logging.error(f'Post request has not been sent.: {e}')


    # --------------------------------------------------------------------------------------
    # GET REQUEST
    # This function receives a JSON file of an order by its endpoint
    # and return a value by a specific key.

    def store_order_by_id(self, id):
        try:
             logging.info("Sending get request to the server.")
             return self._request.get_request(
                f'{self._url}{self.ORDER_BY_ID}{id}')
        except Exception as e:
            logging.error(f'Get request has not been sent.: {e}')