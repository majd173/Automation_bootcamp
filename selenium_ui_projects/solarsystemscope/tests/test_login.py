import unittest
import logging
# tests ---------------------------------infra----------------------------------------files
from selenium_ui_projects.solarsystemscope.infra.config_provider import ConfigProvider
from selenium_ui_projects.solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from selenium_ui_projects.solarsystemscope.logic.home_page import HomePage



class LogInTest(unittest.TestCase):

    # ------------------------------------------------------------------------------------------------------------
    # This function opens the homepage before all tests.
    def setUp(self):
        self.config = ConfigProvider.load_from_file('../solar_config.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)

    # ------------------------------------------------------------------------------------------------------------
    # This function closes the website after all tests.
    def tearDown(self):
        self._driver.close()
        logging.info(f'{self.config["browser"]} browser was closed.')
        logging.info("----------------- TEST DONE ------------------\n")

    # ------------------------------------------------------------------------------------------------------------
    # Testing valid logging in - valid username and valid password.
    # Test case no: 1 - To ensure that a customer can log in successfully using valid details.


    def test_valid_login(self):
        logging.info("_____VALID LOGIN TESTING BEGAN_____")
        logging.info(f'{self.config["browser"]} browser was opened')
        self.home_page.valid_log_in_flow()
        self.assertEqual(True, self.home_page.logout_button_display(),
                         "Wrong login process.")

    # ------------------------------------------------------------------------------------------------------------
    # Testing invalid logging in - invalid username and invalid password.
    # Test case no: 2 - To ensure that a customer can not log in successfully using invalid details.


    def test_invalid_login(self):
        logging.info("_____INVALID LOGIN TESTING BEGAN_____")
        self.home_page.invalid_log_in_flow()
        self.assertEqual("Error:Email or password does not exist.",
            self.home_page.error_login_message_display(),
                         "Wrong invalid login message.")


if __name__ == '__main__':
    unittest.main()