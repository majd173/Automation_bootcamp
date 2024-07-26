import logging
import unittest
from api.pet_store.infra.config_provider import ConfigProvider
from api.pet_store.infra.jira_handler import JiraHandler
from api.pet_store.logic.User.user import UserPage
from api.pet_store.infra.api_wrapper import ApiWrapper
from api.pet_store.logic.entity.user_details import UserDetails
from api.pet_store.infra.utilities import Utils


class TestUser(unittest.TestCase):


    def setUp(self):
        # ARRANGE
        """
        Setting up URL and base details fot adding and getting a username.
        Setting up user details for adding a new user to the list.
        Setting up user details for adding to users database table.
        """
        self._config = ConfigProvider().load_from_file(
            r"C:\Users\Admin\Desktop\Automation_bootcamp\api\pet_store\pet_store.json")
        self._api = ApiWrapper()
        self._pet_store = UserPage(self._api)
        self._jira_flag = JiraHandler()
        self.user_details = UserDetails(
            Utils.generate_random_number(7),
            Utils.generate_random_string_only_letters(5),
            Utils.generate_random_string_only_letters(5),
            Utils.generate_random_string_only_letters(3),
            Utils.generate_random_number(3))
    # --------------------------------------------------------------------------------------

    def tearDown(self):
        self._jira_flag.create_jira_issue_teardown(
            'AABB', 'test_user_login', 'There is a bug, True Not False.', 'Bug')
        logging.info("_______TEST COMPLETED________\n")
    # --------------------------------------------------------------------------------------

    def test_user_login(self):
        """
        Test Case #7: User login.
        Testing acceptance and status code of a request and a received body confirmation.
        """
        logging.info("7_______TEST (USER) BEGAN_______7")
        # ACT
        login_response = self._pet_store.login_user(
            Utils.generate_random_string_only_letters(7),
            Utils.generate_random_number(7),)
        # ASSERT
        self.assertTrue(login_response.ok)
        self.assertEqual(self._config['status_code_passed'], login_response.status_code)
        self.assertEqual(login_response.data['code'], self._config['login_user_code_value'])

    # --------------------------------------------------------------------------------------

    def test_user_logout(self):
        """
        Test Case #8: User logout.
        Testing acceptance and status code of a request and a received body confirmation.
        """
        logging.info("8_______TEST (USER) BEGAN_______8")
        # ACT
        log_out_response = self._pet_store.user_logout()
        # ASSERT
        self.assertTrue(log_out_response.ok)
        self.assertEqual(log_out_response.status_code, self._config['status_code_passed'])
        self.assertEqual(log_out_response.data['message'], self._config['user_logout_message_value'])


    # --------------------------------------------------------------------------------------

    def test_add_users_list(self):
        """
        Test Case #9: Add user to the users list.
        Testing a response of adding a user + acceptance and status code.
        Pre_conditions (adding a new user) is being managed in the setUp function.
        """
        logging.info("9_______TEST (USER) BEGAN_______9")
        self._result_add_user = self._pet_store.create_users_list(self.user_details)
        # ASSERT
        self.assertTrue(self._result_add_user.ok)
        self.assertEqual(self._config['status_code_passed'], self._result_add_user.status_code)
        self.assertEqual(self._result_add_user.data['code'], self._config['add_user_list_value'])
        self.assertEqual(self._result_add_user.data['type'], "unknown")
        self.assertEqual(self._result_add_user.data['message'], "ok")


    # --------------------------------------------------------------------------------------

    def test_get_user_by_username(self):
        """
        Test Case #10: Get user nay username.
        Testing username get details after adding one + acceptance and status code.
        Pre_conditions (adding a new user) is being managed in the setUp function.
        """
        logging.info("10_______TEST (USER) BEGAN_______10")
        get_user_response = self._pet_store.get_user_by_username(self.user_details.username)
        # ASSERT
        self.assertTrue(get_user_response.ok)
        self.assertEqual(self._config['status_code_passed'], get_user_response.status_code)
        self.assertEqual(get_user_response.data['id'], self.user_details.user_id)
        self.assertEqual(get_user_response.data['username'], self.user_details.username)
        self.assertEqual(get_user_response.data['firstName'], self.user_details.firstname)
        self.assertEqual(get_user_response.data['lastName'], self.user_details.lastname)
        self.assertEqual(get_user_response.data['userStatus'], self.user_details.user_status)




if __name__ == '__main__':
    unittest.main()
