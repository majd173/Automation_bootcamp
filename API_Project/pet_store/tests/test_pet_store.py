import unittest
import logging
from API_Project.pet_store.infra.config_provider import ConfigProvider
from API_Project.pet_store.logic.entity.order_details import OrderDetails
from API_Project.pet_store.logic.pet_store_web import PetStoreWeb
from API_Project.pet_store.infra.API_Wrapper import APIWrapper


class TestPetStoreWeb(unittest.TestCase):

    def setUp(self):
        self._config = ConfigProvider().load_from_file("../pet_store.json")
        self._api = APIWrapper()

    def test_pet_by_status(self):
        logging.info("_______TEST (1) BEGAN_______")
        pet_store = PetStoreWeb(self._api)
        result = pet_store.pet_by_status('available')
        result_1 = pet_store.pet_by_status_get_json('id', 'available')  #################
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_1, 3333)  #################

    def test_pet_store_inventory(self):
        logging.info("_______TEST (2) BEGAN_______")
        pet_store = PetStoreWeb(self._api)
        result = pet_store.store_inventory()
        result_1 = pet_store.store_inventory_get_json('sold')
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_1, 4)

    def test_store_order_add(self):
        logging.info("_______TEST (3) BEGAN_______")
        pet_store = PetStoreWeb(self._api)
        my_order_details = OrderDetails(6, 3, 4)
        dictionary = my_order_details.to_dict()
        result = pet_store.store_order_add(dictionary)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)

    def test_store_order_by_id(self):
        logging.info("_______TEST (4) BEGAN_______")
        pet_store = PetStoreWeb(self._api)
        result = pet_store.store_order_by_id(2, 'type')
        self.assertEqual(result, 'error')

    def test_username_get_by_key_value(self):
        logging.info("_______TEST (5) BEGAN_______")
        pet_store = PetStoreWeb(self._api)
        result_1 = pet_store.username_get_by_key_value_1('string')
        result_2 = pet_store.username_get_by_key_value_2('type', 'fail')
        self.assertTrue(result_1.ok)
        self.assertEqual(result_1.status_code, 200)
        self.assertEqual(result_2, 'error')

    def test_login_user(self):
        logging.info("_______TEST (6) BEGAN_______")
        pet_store = PetStoreWeb(self._api)
        result = pet_store.login_user('positive', 123456789, 'code')
        self.assertEqual(result, 200)


if __name__ == '__main__':
    unittest.main()