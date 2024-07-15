import logging
import unittest
# tests ---------------------------------infra----------------------------------------files
from intro_to_selenium.solarsystemscope.infra.config_provider import ConfigProvider
from intro_to_selenium.solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.solarsystemscope.logic.home_page import HomePage


class TestLogout(unittest.TestCase):

    # ------------------------------------------------------------------------------------------------------------
    # This function opens the homepage before all tests.
    def setUp(self):
        self.config = ConfigProvider.load_from_file('../solar_config.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)
        self.home_page.valid_log_in_flow()

    # ------------------------------------------------------------------------------------------------------------
    # This function closes the website after all tests.

    def tearDown(self):
        self._driver.close()
        logging.info(f'{self.config["browser"]} browser was closed.')
        logging.info("----------------- TEST DONE ------------------\n"
        "----------------------------------------------------------------")


    # ------------------------------------------------------------------------------------------------------------
    # Testing logging out successfully.
    # Test case no: 8 - To ensure that a customer can log out successfully after being logged in.

    def test_logout_successfully(self):
        logging.info("_____LOGOUT SUCCESSFULLY TESTING BEGAN_____")
        logging.info(f'{self.config["browser"]} browser was opened')
        self.home_page.click_on_logout_button()
        self.assertTrue(self.home_page.logout_confirmation())
        self._driver.save_screenshot('After clicking logut button.png')


if __name__ == '__main__':
    unittest.main()