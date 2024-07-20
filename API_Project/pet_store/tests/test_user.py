import logging
import unittest
from API_Project.pet_store.infra.config_provider import ConfigProvider
from API_Project.pet_store.logic.User.user import UserPage
from API_Project.pet_store.infra.API_Wrapper import APIWrapper
from API_Project.pet_store.logic.entity.user_details import UserDetails


class TestUser(unittest.TestCase):

    def setUp(self):
        self._config = ConfigProvider().load_from_file("../pet_store.json")
        self._api = APIWrapper()

    # --------------------------------------------------------------------------------------

    def test_username_get(self):
        logging.info("7_______TEST (USER) BEGAN_______7")
        pet_store = UserPage(self._api)
        result_1 = pet_store.username_get_by_key_value_check_st_ok(
            self._config['username_get_by_key_value_name'])
        result_2 = pet_store.username_get_by_key_value(
            self._config['username_get_by_key_value_key'],
            self._config['username_get_by_key_value_name'])
        self.assertTrue(result_1.ok)
        self.assertEqual(result_1.status_code, 200)
        self.assertEqual(result_2, self._config['username_get_by_key_value_value'])
        logging.info("7_______TEST (USER) COMPLETED_______7\n")

    # Testing acceptance and status code of a request and a received body confirmation.
    # --------------------------------------------------------------------------------------

    def test_user_login(self):
        logging.info("8_______TEST (USER) BEGAN_______8")
        pet_store = UserPage(self._api)
        result_1 = pet_store.login_user_check_st_ok(
            self._config['login_user_name'],
            self._config['login_user_password'])
        result_2 = pet_store.login_user(
            self._config['login_user_name'],
            self._config['login_user_password'],
            self._config['login_user_key'])
        self.assertTrue(result_1.ok)
        self.assertEqual(result_1.status_code, 200)
        self.assertEqual(result_2, self._config['login_user_value'])
        logging.info("8_______TEST (USER) COMPLETED_______8\n")

    # Testing acceptance and status code of a request and a received body confirmation.
    # --------------------------------------------------------------------------------------

    def test_user_logout(self):
        logging.info("9_______TEST (USER) BEGAN_______9")
        pet_store = UserPage(self._api)
        result_1 = pet_store.user_logout_check_st_ok()
        result_2 = pet_store.user_logout_message(
            self._config['user_logout_message_key'])
        self.assertTrue(result_1.ok)
        self.assertEqual(result_1.status_code, 200)
        self.assertEqual(result_2, self._config['user_logout_message_value'])
        logging.info("9_______TEST (USER) COMPLETED_______9\n")

    # Testing acceptance and status code of a request and a received body confirmation.
    # --------------------------------------------------------------------------------------

    def test_add_users_list(self):
        logging.info("10_______TEST (USER) BEGAN_______10")
        pet_store = UserPage(self._api)
        user_details = UserDetails(
            self._config['add_users_list_id'],
            self._config['add_users_list_username'],
            self._config['add_users_list_firstname'],
            self._config['add_users_list_lastname'])
        dictionary = user_details.to_dict()
        result = pet_store.create_users_list(dictionary)
        added_user_firstname = dictionary[1]['firstName']
        self.assertTrue(result.ok)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(added_user_firstname, self._config['add_users_list_firstname'])

        # Testing adding new user to the list of users.


if __name__ == '__main__':
    unittest.main()
