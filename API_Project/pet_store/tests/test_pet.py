import unittest
import logging
from API_Project.pet_store.infra.config_provider import ConfigProvider
from API_Project.pet_store.logic.Pet.pet import PetPage
from API_Project.pet_store.infra.API_Wrapper import APIWrapper



class TestPet(unittest.TestCase):

    def setUp(self):
        self._config = ConfigProvider().load_from_file("../pet_store.json")
        self._api = APIWrapper()

    def test_pet_by_status(self):
        logging.info("_______TEST (1) BEGAN_______")
        pet_store = PetPage(self._api)
        result_2 = pet_store.pet_by_status_get_json(
            self._config['pet_by_status_key'],
            self._config['pet_by_status_endpoint'])
        self.assertEqual(result_2, self._config['pet_by_status_value'])
        logging.info("_______TEST (1) COMPLETED_______\n")


if __name__ == '__main__':
    unittest.main()
