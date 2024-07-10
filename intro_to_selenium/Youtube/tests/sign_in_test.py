import time
import unittest
from intro_to_selenium.para_bank.infra.config_provider import ConfigProvider
from intro_to_selenium.para_bank.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.para_bank.logic.home_page import HomePage
from intro_to_selenium.solarsystemscope.logic.log_in import LogIn
from intro_to_selenium.solarsystemscope.logic.final_log_in import FinalLogIn




class TestSignIn(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider.load_from_file('../../solarsystemscope/config.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)

    #opening the homepage before all tests

    def tearDown(self):
        self._driver.close()
    # closing the website after all tests

    def test_invalid_sign_in(self):
        print("VALID LOG_IN TESTING BEGAN...")
        self.home_page.go_to_log_in()
        log_in = LogIn(self._driver)
        log_in.log_in_flow()
        final_log_in = FinalLogIn(self._driver)
        final_log_in.final_log_in()

        time.sleep(3) # In order to see the needed "Invalid sign in".
        print("--------------------------------------------")
        # Tests signing in using invalid generated phone number includes only 9 numbers.

