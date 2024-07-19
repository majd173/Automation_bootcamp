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

    def test_username_get(self):
        logging.info("7_______TEST (USER) BEGAN_______7")
        pet_store = UserPage(self._api)
        result_1 = pet_store.username_get_by_key_value(
            self._config['username_get_by_key_value_key'],
            self._config['username_get_by_key_value_name'])
        result_2 = pet_store.username_get_by_key_value_check_st_ok(
            self._config['username_get_by_key_value_name'])
        self.assertEqual(result_1, self._config['username_get_by_key_value_value'])
        self.assertTrue(result_2.ok)
        self.assertEqual(result_2.status_code, 200)
        logging.info("7_______TEST (USER) COMPLETED_______7\n")

    # --------------------------------------------------------------------------------------

    def test_user_login(self):
        logging.info("8_______TEST (USER) BEGAN_______8")
        pet_store = UserPage(self._api)
        result_1 = pet_store.login_user(
            self._config['login_user_name'],
            self._config['login_user_password'],
            self._config['login_user_key'])
        result_2 = pet_store.login_user_check_st_ok(
            self._config['login_user_name'],
            self._config['login_user_password'])
        self.assertTrue(result_2.ok)
        self.assertEqual(result_2.status_code, 200)
        self.assertEqual(result_1, self._config['login_user_value'])
        logging.info("8_______TEST (USER) COMPLETED_______8\n")

    # --------------------------------------------------------------------------------------

    def test_user_logout(self):
        logging.info("9_______TEST (USER) BEGAN_______9")
        pet_store = UserPage(self._api)
        result_1 = pet_store.user_logout_check_st_ok()
        result_2 = pet_store.user_logout_message(
            self._config['user_logout_message_key'])
        self.assertTrue(result_1.ok)
        self.assertEqual(result_1.status_code, 200)
        self.assertEqual(result_2, 'ok')
        logging.info("9_______TEST (USER) COMPLETED_______9\n")




if __name__ == '__main__':
    unittest.main()
