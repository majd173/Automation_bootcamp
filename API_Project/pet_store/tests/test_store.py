import unittest
import logging
from API_Project.pet_store.infra.config_provider import ConfigProvider
from API_Project.pet_store.infra.utilities import Utils
from API_Project.pet_store.logic.Store.store import StorePage
from API_Project.pet_store.infra.API_Wrapper import APIWrapper
from API_Project.pet_store.logic.entity.order_details import OrderDetails

class TestStore(unittest.TestCase):

    def setUp(self):
        """
        Setting up URL and base details fot adding and getting a username.
        """
        self._config = ConfigProvider().load_from_file("../pet_store.json")
        self._api = APIWrapper()
        self._pet_store = StorePage(self._api)
        self._order_details = OrderDetails(
            Utils.generate_random_number(2),
            Utils.generate_random_number(2),
            Utils.generate_random_number(6))
        self._order_response = self._pet_store.store_order_add(self._order_details)


    # --------------------------------------------------------------------------------------

    def test_pet_store_inventory(self):
        """
        Test Case #4: Store inventory.
        Testing acceptance and status code of a request and a received body confirmation.
        """
        logging.info("4_______TEST (STORE) BEGAN_______4")
        pet_store = StorePage(self._api)
        response = pet_store.store_inventory()
        self.assertTrue(response.ok)
        self.assertEqual(self._config['status_code_passed'], response.status_code)
        self.assertIn(self._config['inventory_sold'], response.data)
        self.assertIn(self._config['inventory_available'], response.data)
        logging.info("4_______TEST (STORE) COMPLETED_______4\n")

    # --------------------------------------------------------------------------------------

    def test_store_order_add(self):
        """
        Test Case #5: Add an order.
        Testing acceptance and status and body information of a request after submitting a post.
        """
        logging.info("5_______TEST (STORE) BEGAN_______5")
        self.assertTrue(self._order_response.ok)
        self.assertEqual(self._config['status_code_passed'], self._order_response.status_code)
        self.assertEqual(self._order_response.data['id'], self._order_details.order_id)
        self.assertEqual(self._order_response.data['petId'], self._order_details.pet_id)
        self.assertEqual(self._order_response.data['quantity'], self._order_details.quantity)
        logging.info("5_______TEST (STORE) COMPLETED_______5\n")

    # --------------------------------------------------------------------------------------

    def test_store_order_get(self):
        """
        Test Case #6: Store order.
        Testing request received of an order by its id.
        """
        logging.info("6_______TEST (STORE) BEGAN_______6")
        get_response = self._pet_store.store_order_by_id(self._order_details.order_id)
        self.assertEqual(get_response.data["id"], self._order_details.order_id)
        self.assertEqual(get_response.data["petId"], self._order_details.pet_id)
        self.assertEqual(get_response.data["quantity"], self._order_details.quantity)
        logging.info("6_______TEST (STORE) COMPLETED_______6\n")



if __name__ == '__main__':
    unittest.main()
