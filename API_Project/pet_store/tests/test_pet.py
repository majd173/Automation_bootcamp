import unittest
import logging
from API_Project.pet_store.infra.config_provider import ConfigProvider
from API_Project.pet_store.logic.Pet.pet import PetPage
from API_Project.pet_store.infra.API_Wrapper import APIWrapper
from API_Project.pet_store.logic.entity.pet_details import PetDetails



class TestPet(unittest.TestCase):

    def setUp(self):
        self._config = ConfigProvider().load_from_file("../pet_store.json")
        self._api = APIWrapper()

    def test_pet_by_status(self):
        logging.info("_______TEST (1) BEGAN_______")
        pet_store = PetPage(self._api)
        result = pet_store.pet_by_status_get_json(
            self._config['pet_by_status_key'],
            self._config['pet_by_status_endpoint'])
        self.assertEqual(result, self._config['pet_by_status_value'])
        logging.info("_______TEST (1) COMPLETED_______\n")


    def test_add_pet(self):
        logging.info("_______TEST (2) BEGAN_______")
        pet_store = PetPage(self._api)
        pet_details = PetDetails(
            self._config['add_pet_id'],
            self._config['add_pet_name'])
        dictionary = pet_details.to_dic()
        result = pet_store.add_pet(dictionary)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)



if __name__ == '__main__':
    unittest.main()
