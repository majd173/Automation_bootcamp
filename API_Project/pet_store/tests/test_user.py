import logging
import unittest
from API_Project.pet_store.infra.config_provider import ConfigProvider
from API_Project.pet_store.logic.User.user import UserPage
from API_Project.pet_store.infra.API_Wrapper import APIWrapper


class TestUser(unittest.TestCase):

    def setUp(self):
        self._config = ConfigProvider().load_from_file("../pet_store.json")
        self._api = APIWrapper()

    # --------------------------------------------------------------------------------------

    def test_username_get_by_key_value(self):
        logging.info("7_______TEST (USER) BEGAN_______7")
        pet_store = UserPage(self._api)
        result = pet_store.username_get_by_key_value(
            self._config['username_get_by_key_value_key'],
            self._config['username_get_by_key_value_name'])
        self.assertEqual(result, self._config['username_get_by_key_value_value'])
        logging.info("7_______TEST (USER) COMPLETED_______7\n")

    # --------------------------------------------------------------------------------------

    def test_login_user(self):
        logging.info("8_______TEST (USER) BEGAN_______8")
        pet_store = UserPage(self._api)
        result = pet_store.login_user(
            self._config['login_user_name'],
            self._config['login_user_password'],
            self._config['login_user_key'])
        self.assertEqual(result, self._config['login_user_value'])
        logging.info("8_______TEST (USER) COMPLETED_______8\n")

    # --------------------------------------------------------------------------------------

    def test_user_logout(self):
        logging.info("9_______TEST (USER) BEGAN_______9")
        pet_store = UserPage(self._api)
        result = pet_store.user_logout()
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        logging.info("9_______TEST (USER) COMPLETED_______9\n")

    # --------------------------------------------------------------------------------------

    def test_user_logout_message(self):
        logging.info("10_______TEST (USER) BEGAN_______10")
        pet_store = UserPage(self._api)
        result = pet_store.user_logout_message(
            self._config['user_logout_message_key'])
        self.assertEqual(result, 'ok')
        logging.info("10_______TEST (USER) COMPLETED_______10\n")





if __name__ == '__main__':
    unittest.main()
