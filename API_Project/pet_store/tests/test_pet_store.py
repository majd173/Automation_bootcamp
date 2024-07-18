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



    def test_pet_by_status_available(self):
        pet_store = PetStoreWeb(self._api)
        result = pet_store.pet_by_status_available()
        result_1 = pet_store.pet_by_status_available_get_json()
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_1('id'), '9223372036854687000')


    def test_pet_store_inventory(self):
        pet_store = PetStoreWeb(self._api)
        result = pet_store.store_inventory()
        result_1 = pet_store.store_inventory_get_json()
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result_1('sold'), 2)


    # def test_store_order_add(self):
    #     pet_store = PetStoreWeb(self._api)
    #     my_order_details = OrderDetails(6,3,4)
    #     result = pet_store.store_order_add(my_order_details)
    #     print(result.status_code)
    #     self.assertTrue(result.ok)

    def test_store_order_by_id(self):
        pet_store = PetStoreWeb(self._api)
        result = pet_store.store_order_by_id(2)
        self.assertEqual(result, 2)



