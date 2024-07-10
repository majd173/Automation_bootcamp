import unittest
from intro_to_selenium.solarsystemscope.infra.config_provider import ConfigProvider
from intro_to_selenium.solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.solarsystemscope.logic.home_page import HomePage
from intro_to_selenium.solarsystemscope.logic.login_confirmation.login_successfully import LogInSuccessfully
from intro_to_selenium.solarsystemscope.logic.login_confirmation.login_unsuccessfully import LogInUnsuccessfully



class LogInTest(unittest.TestCase):


    def setUp(self):
        self.config = ConfigProvider.load_from_file('../config.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)

    #opening the homepage before all tests

    def tearDown(self):
        self._driver.close()
    # closing the website after all tests

    def test_valid_login(self):
        print("VALID LOGIN TESTING BEGAN...")
        self.home_page.valid_log_in_flow()
        logged_in = LogInSuccessfully(self._driver)
        self.assertEqual(True, logged_in.logout_button_display(), "WRONG LOGIN MESSAGE.")
        print("--------------------------------------------")
        # Testing valid login - valid username and valid password.


    def test_invalid_login(self):
        print("INVALID LOGIN TESTING BEGAN...")
        self.home_page.invalid_log_in_flow()
        fail_login = LogInUnsuccessfully(self._driver)
        self.assertEqual("Error:Email or password does not exist.", fail_login.error_message_display(), "WRONG LOGIN MESSAGE.")
        print("--------------------------------------------")
        # Testing invalid login - invalid username and invalid password.