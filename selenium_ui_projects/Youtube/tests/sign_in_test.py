import time
import unittest
from selenium_ui_projects.Youtube.infra.config_provider import ConfigProvider
from selenium_ui_projects.Youtube.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from selenium_ui_projects.Youtube.logic.home_page import HomePage
from selenium_ui_projects.Youtube.logic.sign_in import SignIn
from selenium_ui_projects.Youtube.logic.invalid_sign_in import InvalidLogIn




class TestSignIn(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider.load_from_file('../config.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)

    #opening the homepage before all tests

    def tearDown(self):
        self._driver.close()
    # closing the website after all tests

    def test_invalid_sign_in(self):
        print("INVALID LOG_IN TESTING BEGAN...")
        self.home_page.go_to_sign_in()
        log_in = SignIn(self._driver)
        log_in.sign_in_flow()
        final_log_in = InvalidLogIn(self._driver)
        final_log_in.error_return()
        time.sleep(3) # In order to see the needed "Invalid sign in".
        print("--------------------------------------------")
        # Tests signing in using invalid generated phone number includes only 9 numbers.

