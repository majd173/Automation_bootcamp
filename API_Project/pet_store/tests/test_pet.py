import unittest
import logging
from API_Project.pet_store.infra.config_provider import ConfigProvider
from API_Project.pet_store.logic.Pet.pet import PetPage
from API_Project.pet_store.infra.API_Wrapper import APIWrapper
from API_Project.pet_store.logic.entity.pet_details import PetDetails
from API_Project.pet_store.infra.utilities import Utils
from API_Project.pet_store.logic.enums.enums import Enums, generate_a_status


class TestPet(unittest.TestCase):

    def setUp(self):
        self._config = ConfigProvider().load_from_file("../pet_store.json")
        self._api = APIWrapper()
        self._pet_store = PetPage(self._api)
        self._pet_details = PetDetails(
            Utils.generate_random_number(4),
            Utils.generate_random_string_only_letters(6))

    # Setting up URL and base details fot adding and getting a username.
    # --------------------------------------------------------------------------------------

    def test_pet_by_status(self):
        logging.info("1_______TEST (PET]) BEGAN_______1")
        pet_store = PetPage(self._api)
        status = generate_a_status()
        response = pet_store.pet_by_status(status)
        status_value = response.json()[1]['status']
        self.assertTrue(response.ok)
        self.assertEqual(200, response.status_code)
        self.assertEqual(status_value, status)
        logging.info("1_______TEST (PET) COMPLETED_______1\n")

    # Testing acceptance and status code of a request and a received body confirmation.

    # --------------------------------------------------------------------------------------

    def test_add_pet(self):
        logging.info("2_______TEST (PET) BEGAN_______2")
        result_add_pet = self._pet_store.add_pet(self._pet_details)
        result_get_pet = self._pet_store.get_pet_by_id(self._pet_details.pet_id)
        self.assertTrue(result_add_pet.ok)
        self.assertEqual(result_add_pet.status_code, 200)
        self.assertEqual(result_get_pet.json()['id'], self._pet_details.pet_id)
        logging.info("2_______TEST (PET) COMPLETED_______2\n")

    # Testing acceptance and status code of a request after submitting a post.

    # --------------------------------------------------------------------------------------

    # def test_delete_pet(self):
    #     logging.info("3_______TEST (PET) BEGAN_______3")
    #     delete_response = self._pet_store.delete_pet(
    #         self._pet_details,
    #         self._pet_details.pet_id)
    #     self.assertEqual(delete_response['message'], self._pet_details.pet_id)
    #     logging.info("3_______TEST (PET) COMPLETED_______3\n")

    # Testing request received body confirmation after submitting a post
    # followed by a delete process.


if __name__ == '__main__':
    unittest.main()
