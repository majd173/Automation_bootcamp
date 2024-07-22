import sys
import logging
import unittest
from API_Project.pet_store.infra.config_provider import ConfigProvider
from API_Project.pet_store.logic.User.user import UserPage
from API_Project.pet_store.infra.API_Wrapper import APIWrapper
from API_Project.pet_store.logic.entity.user_details import UserDetails
from API_Project.pet_store.infra.utilities import Utils


class TestUser(unittest.TestCase):
    sys.setrecursionlimit(1500)

    def setUp(self):
        self._config = ConfigProvider().load_from_file("../pet_store.json")
        self._api = APIWrapper()
        self._pet_store = UserPage(self._api)
        self.user_details = UserDetails(
            Utils.generate_random_number(7),
            Utils.generate_random_string_only_letters(5),
            Utils.generate_random_string_only_letters(5),
            Utils.generate_random_string_only_letters(3),
            Utils.generate_random_number(3))
        self._result_add_user = self._pet_store.create_users_list(self.user_details)

    # Setting up URL and base details fot adding and getting a username.
    # --------------------------------------------------------------------------------------

    def test_user_login(self):
        logging.info("7_______TEST (USER) BEGAN_______7")
        pet_store = UserPage(self._api)
        response = pet_store.login_user(
            Utils.generate_random_string_only_letters(7),
            Utils.generate_random_number(7),)
        self.assertTrue(response.ok)
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json()['code'], self._config['login_user_value'])
        logging.info("7_______TEST (USER) COMPLETED_______7\n")

    # Testing acceptance and status code of a request and a received body confirmation.
    # --------------------------------------------------------------------------------------

    def test_user_logout(self):
        logging.info("8_______TEST (USER) BEGAN_______8")
        pet_store = UserPage(self._api)
        response = pet_store.user_logout()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], self._config['user_logout_message_value'])
        logging.info("8_______TEST (USER) COMPLETED_______8\n")

    # Testing acceptance and status code of a request and a received body confirmation.
    # --------------------------------------------------------------------------------------

    def test_add_users_list(self):
        logging.info("9_______TEST (USER) BEGAN_______9")
        self.assertTrue(self._result_add_user.ok)
        self.assertEqual(200, self._result_add_user.status_code)
        self.assertEqual(self._result_add_user.json()['code'], 200)
        self.assertEqual(self._result_add_user.json()['type'], "unknown")
        self.assertEqual(self._result_add_user.json()['message'], "ok")
        logging.info("9_______TEST (USER) COMPLETED_______9\n")

        # Testing a response of adding a user + acceptance and status code.
    # --------------------------------------------------------------------------------------

    def test_get_user_by_username(self):
        logging.info("10_______TEST (USER) BEGAN_______10")
        get_user_response = self._pet_store.get_user_by_username(self.user_details.username)
        data = get_user_response.json()
        self.assertTrue(get_user_response.ok)
        self.assertEqual(200, get_user_response.status_code)
        self.assertEqual(data['id'], self.user_details.user_id)
        self.assertEqual(data['username'], self.user_details.username)
        self.assertEqual(data['firstName'], self.user_details.firstname)
        self.assertEqual(data['lastName'], self.user_details.lastname)
        self.assertEqual(data['userStatus'], self.user_details.user_status)
        logging.info("10_______TEST (USER) COMPLETED_______10\n")

        # Testing username get details after adding one + acceptance and status code.




if __name__ == '__main__':
    unittest.main()
