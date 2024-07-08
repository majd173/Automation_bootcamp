import time
import unittest
from intro_to_selenium.para_bank.infra.config_provider import ConfigProvider
from intro_to_selenium.para_bank.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.Youtube.logic.home_page import HomePage
from intro_to_selenium.Youtube.logic.sign_in import SignIn
from intro_to_selenium.Youtube.logic.invalid_sign_in import InvalidLogIn



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
        print("Invalid log_in testing began...")
        self.home_page.go_to_sign_in()
        sign_in = SignIn(self._driver)
        sign_in.sign_in_flow()
        message = InvalidLogIn(self._driver)
        message.error_return()
        self.assertTrue(message.error_return())
        time.sleep(3) # In order to see the needed "Invalid sign in".
        print("--------------------------------------------")
        # Tests signing in using invalid generated phone number includes only 9 numbers.

