import unittest
import logging
from API_Project.pet_store.infra.config_provider import ConfigProvider
from API_Project.pet_store.infra.utilities import Utils
from API_Project.pet_store.logic.Store.store import StorePage
from API_Project.pet_store.infra.API_Wrapper import APIWrapper
from API_Project.pet_store.logic.entity.order_details import OrderDetails


class TestStore(unittest.TestCase):

    def setUp(self):
        self._config = ConfigProvider().load_from_file("../pet_store.json")
        self._api = APIWrapper()
        self._pet_store = StorePage(self._api)
        self._order_details = OrderDetails(
            Utils.generate_random_number(2),
            Utils.generate_random_number(2),
            Utils.generate_random_number(6))
        self._order_response = self._pet_store.store_order_add(self._order_details)

    # Setting up URL and base details fot adding and getting a username.
    # --------------------------------------------------------------------------------------

    def test_pet_store_inventory(self):
        logging.info("4_______TEST (STORE) BEGAN_______4")
        pet_store = StorePage(self._api)
        response = pet_store.store_inventory()
        pending_value = response.json()['pending']
        self.assertTrue(response.ok)
        self.assertEqual(200, response.status_code)
        self.assertEqual(pending_value, self._config['pet_store_inventory_value'])
        logging.info("4_______TEST (STORE) COMPLETED_______4\n")

    # Testing acceptance and status code of a request and a received body confirmation.

    # --------------------------------------------------------------------------------------

    def test_store_order_add(self):
        logging.info("5_______TEST (STORE) BEGAN_______5")
        self.assertTrue(self._order_response.ok)
        self.assertEqual(200, self._order_response.status_code)
        self.assertEqual(self._order_response.json()['id'], self._order_details.order_id)
        self.assertEqual(self._order_response.json()['petId'], self._order_details.pet_id)
        self.assertEqual(self._order_response.json()['quantity'], self._order_details.quantity)
        logging.info("5_______TEST (STORE) COMPLETED_______5\n")

    # Testing acceptance and status and body information of a request after submitting a post.

    # --------------------------------------------------------------------------------------

    def test_store_order_get(self):
        logging.info("6_______TEST (STORE) BEGAN_______6")
        get_response = self._pet_store.store_order_by_id(self._order_details.order_id)
        self.assertEqual(get_response.json()["id"], self._order_details.order_id)
        self.assertEqual(get_response.json()["petId"], self._order_details.pet_id)
        self.assertEqual(get_response.json()["quantity"], self._order_details.quantity)
        logging.info("6_______TEST (STORE) COMPLETED_______6\n")

    # Testing request received of an order by its id.




if __name__ == '__main__':
    unittest.main()
