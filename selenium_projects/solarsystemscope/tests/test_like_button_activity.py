import logging
import unittest
# tests ---------------------------------infra----------------------------------------files
from selenium_projects.solarsystemscope.infra.config_provider import ConfigProvider
from selenium_projects.solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from selenium_projects.solarsystemscope.logic.home_page import HomePage

class TestLikeButtonActivity(unittest.TestCase):

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
    # Testing Like button activity.
    # Test case no: 7 - To ensure that a customer can click the "Like" button.

    def test_like_button_activity(self):
        logging.info("_____LIKE BUTTON ACTIVITY TESTING BEGAN_____")
        logging.info(f'{self.config["browser"]} browser was opened')
        self.home_page.click_on_like_button()
        self.assertTrue(self.home_page.check_like_button_activity())



if __name__ == '__main__':
    unittest.main()
