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

    # --------------------------------------------------------------------------------------

    def test_pet_by_status(self):
        logging.info("1_______TEST (PET]) BEGAN_______1")
        pet_store = PetPage(self._api)
        result_1 = pet_store.pet_by_status_check_st_ok(
            self._config['pet_by_status_endpoint'])
        result_2 = pet_store.pet_by_status_get_json(
            self._config['pet_by_status_key'],
            self._config['pet_by_status_endpoint'])
        self.assertTrue(result_1.ok)
        self.assertEqual(result_1.status_code, 200)
        self.assertEqual(result_2, self._config['pet_by_status_value'])
        logging.info("1_______TEST (PET) COMPLETED_______1\n")

    # --------------------------------------------------------------------------------------

    def test_add_pet(self):
        logging.info("2_______TEST (PET) BEGAN_______2")
        pet_store = PetPage(self._api)
        pet_details = PetDetails(
            self._config['add_pet_id'],
            self._config['add_pet_name'])
        dictionary = pet_details.to_dic()
        result = pet_store.add_pet(dictionary)
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        logging.info("2_______TEST (PET) COMPLETED_______2\n")

    # --------------------------------------------------------------------------------------

    def test_delete_pet(self):
        logging.info("3_______TEST (PET) BEGAN_______3")
        pet_store = PetPage(self._api)
        pet_details = PetDetails(
            self._config['add_pet_id'],
            self._config['add_pet_name'])
        dictionary = pet_details.to_dic()
        result = pet_store.delete_pet(
            dictionary, self._config['delete_user_key'])
        self.assertEqual(result, self._config['delete_user_value'])
        logging.info("3_______TEST (PET) COMPLETED_______3\n")



if __name__ == '__main__':
    unittest.main()
