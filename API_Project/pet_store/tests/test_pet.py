import unittest
import logging
from API_Project.pet_store.infra.config_provider import ConfigProvider
from API_Project.pet_store.logic.Pet.pet import PetPage
from API_Project.pet_store.infra.API_Wrapper import APIWrapper
from API_Project.pet_store.logic.entity.pet_details import PetDetails
from API_Project.pet_store.infra.utilities import Utils
from API_Project.pet_store.logic.enums.enums_class import Enums


class TestPet(unittest.TestCase):

    def setUp(self):
        # ARRANGE
        self._config = ConfigProvider().load_from_file("../pet_store.json")
        self._api = APIWrapper()
        self._pet_store = PetPage(self._api)
        self._pet_details = PetDetails(
            Utils.generate_random_number(4),
            Utils.generate_random_string_only_letters(6))

    # Setting up URL and base details fot adding and getting a username.
    # --------------------------------------------------------------------------------------

    def test_get_pet_by_status(self):
        """
        Test Case #1: Get pet by status.
        Testing acceptance and status code of a request and a received body confirmation.
        """
        logging.info("1_______TEST (PET]) BEGAN_______1")
        pet_store = PetPage(self._api)
        status = Enums.generate_a_status()
        print(status)
        # ACT
        response = pet_store.pet_by_status(status)
        status_value = response.data[1]['status']
        # ASSERT
        self.assertTrue(response.ok)
        self.assertEqual(self._config['status_code_passed'], response.status_code)
        self.assertEqual(status_value, status)
        logging.info("1_______TEST (PET) COMPLETED_______1\n")


    # --------------------------------------------------------------------------------------

    def test_add_pet(self):
        """
        Test Case #2: Add a pet.
        Testing acceptance and status code of a request after submitting a post.
        """
        logging.info("2_______TEST (PET) BEGAN_______2")
        # ACT
        response_add_pet = self._pet_store.add_pet(self._pet_details)
        # ASSERT
        self.assertTrue(response_add_pet.ok)
        self.assertEqual(response_add_pet.status_code, self._config['status_code_passed'])
        logging.info("2_______TEST (PET) COMPLETED_______2\n")

    # --------------------------------------------------------------------------------------

    def test_get_pet_by_id(self):
        """
        Test Case #3: Get a pet by id.
        Testing acceptance and status code of a request and a received body confirmation.
         """
        logging.info("3_______TEST (PET) BEGAN_______3")
        # ACT
        response_get_pet = self._pet_store.get_pet_by_id(self._config['get_pet_by_id'])
        status_value = response_get_pet.data['status']
        # ASSERT
        self.assertTrue(response_get_pet.ok)
        self.assertEqual(response_get_pet.status_code, self._config['status_code_passed'])
        self.assertEqual(status_value, self._config['get_pet_by_id_status_value'])
        logging.info("3_______TEST (PET) COMPLETED")



if __name__ == '__main__':
    unittest.main()
