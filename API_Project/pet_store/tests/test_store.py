import unittest
import logging
from API_Project.pet_store.infra.config_provider import ConfigProvider
from API_Project.pet_store.logic.Store.store import StorePage
from API_Project.pet_store.infra.API_Wrapper import APIWrapper
from API_Project.pet_store.logic.entity.order_details import OrderDetails


class TestStore(unittest.TestCase):

    def setUp(self):
        self._config = ConfigProvider().load_from_file("../pet_store.json")
        self._api = APIWrapper()

    # --------------------------------------------------------------------------------------

    def test_pet_store_inventory(self):
        logging.info("4_______TEST (STORE) BEGAN_______4")
        pet_store = StorePage(self._api)
        result_1 = pet_store.store_inventory_check_st_ok()
        result_2 = pet_store.store_inventory(
            self._config['pet_store_inventory_key'])
        self.assertTrue(result_1.ok)
        self.assertEqual(result_1.status_code, 200)
        self.assertEqual(result_2, self._config['pet_store_inventory_value'])
        logging.info("4_______TEST (STORE) COMPLETED_______4\n")

    # Testing acceptance and status code of a request and a received body confirmation.

    # --------------------------------------------------------------------------------------

    def test_store_order_add(self):
        logging.info("5_______TEST (STORE) BEGAN_______5")
        pet_store = StorePage(self._api)
        my_order_details = OrderDetails(
            self._config['store_order_add_id'],
            self._config['store_order_add_pet_id'],
            self._config['store_order_add_quantity'])
        dictionary = my_order_details.to_dict()
        result = pet_store.store_order_add(dictionary)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        logging.info("5_______TEST (STORE) COMPLETED_______5\n")

    # Testing acceptance and status code of a request after submitting a post.

    # --------------------------------------------------------------------------------------

    def test_store_order(self):
        logging.info("6_______TEST (STORE) BEGAN_______6")
        pet_store = StorePage(self._api)
        result = pet_store.store_order_by_id(
            self._config['store_order_by_id_endpoint'],
            self._config['store_order_by_id_key'])
        self.assertEqual(result, self._config['store_order_by_id_value'])
        logging.info("6_______TEST (STORE) COMPLETED_______6\n")

    # Testing request received body confirmation.




if __name__ == '__main__':
    unittest.main()
