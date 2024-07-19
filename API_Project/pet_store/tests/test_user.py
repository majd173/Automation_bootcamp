import logging
import unittest
from API_Project.pet_store.infra.config_provider import ConfigProvider
from API_Project.pet_store.logic.User.user import UserPage
from API_Project.pet_store.infra.API_Wrapper import APIWrapper


class TestUser(unittest.TestCase):

    def setUp(self):
        self._config = ConfigProvider().load_from_file("../pet_store.json")
        self._api = APIWrapper()

    def test_username_get_by_key_value(self):
        logging.info("_______TEST (1) BEGAN_______")
        pet_store = UserPage(self._api)
        result = pet_store.username_get_by_key_value(
            self._config['username_get_by_key_value_key'],
            self._config['username_get_by_key_value_name'])
        self.assertEqual(result, self._config['username_get_by_key_value_value'])
        logging.info("_______TEST (1) COMPLETED_______\n")

    def test_login_user(self):
        logging.info("_______TEST (2) BEGAN_______")
        pet_store = UserPage(self._api)
        result = pet_store.login_user(
            self._config['login_user_name'],
            self._config['login_user_password'],
            self._config['login_user_key'])
        self.assertEqual(result, self._config['login_user_value'])
        logging.info("_______TEST (2) COMPLETED_______\n")

    def test_delete_user_by_name(self):
        logging.info("_______TEST (3) BEGAN_______") ################
        pet_store = UserPage(self._api)
        result = pet_store.delete_user_by_name('string')
        self.assertEqual(result.status_code, 200)
        self.assertFalse(result.ok)
        logging.info("_______TEST (3) COMPLETED_______\n")

if __name__ == '__main__':
    unittest.main()
