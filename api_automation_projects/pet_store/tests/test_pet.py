import unittest
import logging
from api_automation_projects.pet_store.infra.config_provider import ConfigProvider
from api_automation_projects.pet_store.infra.jira_handler import JiraHandler
from api_automation_projects.pet_store.logic.Pet.pet import PetPage
from api_automation_projects.pet_store.infra.api_wrapper import ApiWrapper
from api_automation_projects.pet_store.logic.entity.pet_details import PetDetails
from api_automation_projects.pet_store.infra.utilities import Utils
from api_automation_projects.pet_store.logic.status_generate.status_generate import StatusGenerate


class TestPet(unittest.TestCase):

    def setUp(self):
        """
        Arrange: Setting up an url.
                 Setting up a jira handler.
                 Setting up pet details.
        """
        self._config = ConfigProvider().load_from_file(
            r"/api_automated_testing\pet_store\pet_store.json")
        self._api = ApiWrapper()
        self._pet_store = PetPage(self._api)
        self._jira_flag = JiraHandler()
        self._pet_details = PetDetails(
            Utils.generate_random_number(4),
            Utils.generate_random_string_only_letters(6))
    # Setting up URL and base details fot adding and getting a username.

    def tearDown(self):
        """
        Logging that the test is completed and creating a jira issue.
        """
        # self._jira_flag.create_issue(
        #     self._config['jira_key'], 'test_add_pet',
        #     'Make sure to add pet to the database.', 'Task')
        logging.info("_______TEST COMPLETED_______")

    # --------------------------------------------------------------------------------------

    def test_get_pet_by_status(self):
        """
        Test Case #1: Get pet by status.
        Testing acceptance and status code of a request and a received body confirmation.
        """
        logging.info("1_______TEST (PET]) BEGAN_______1")
        # ARRANGE
        pet_status = StatusGenerate.generate_a_status()
        # ACT
        get_pet_response = self._pet_store.pet_by_status(pet_status)
        status_value = get_pet_response.data[1]['status']
        # ASSERT
        self.assertTrue(get_pet_response.ok)
        self.assertEqual(self._config['status_code_passed'], get_pet_response.status_code)
        self.assertEqual(status_value, pet_status)


    # --------------------------------------------------------------------------------------

    def test_add_pet(self):
        """
        Test Case #2: Add a pet.
        Testing acceptance and status code of a request after submitting a post.
        """
        logging.info("2_______TEST (PET) BEGAN_______2")
        # ACT
        add_pet_response = self._pet_store.add_pet(self._pet_details)
        # ASSERT
        self.assertTrue(add_pet_response.ok)
        self.assertEqual(add_pet_response.status_code, self._config['status_code_passed'])
        self.assertDictEqual(add_pet_response.data, self._pet_details.to_dic())

    # --------------------------------------------------------------------------------------

    def test_get_pet_by_id(self):
        """
        Test Case #3: Get a pet by id.
        Testing acceptance and status code of a request and a received body confirmation.
         """
        logging.info("3_______TEST (PET) BEGAN_______3")
        # ACT
        get_pet_response = self._pet_store.get_pet_by_id(self._config['get_pet_by_id'])
        status_value = get_pet_response.data['status']
        # ASSERT
        self.assertTrue(get_pet_response.ok)
        self.assertEqual(get_pet_response.status_code, self._config['status_code_passed'])



if __name__ == '__main__':
    unittest.main()
