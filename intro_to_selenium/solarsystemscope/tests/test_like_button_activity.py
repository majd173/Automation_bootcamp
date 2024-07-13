import logging
import unittest
import unittest
from intro_to_selenium.solarsystemscope.infra.config_provider import ConfigProvider
from intro_to_selenium.solarsystemscope.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.solarsystemscope.infra.logging_setup import LoggingSetup
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.solarsystemscope.logic.home_page import HomePage

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
    # closing the website after all tests

    # ------------------------------------------------------------------------------------------------------------

    def test_like_button_activity(self):
        logging.info("LIKE BUTTON ACTIVITY TESTING BEGAN...")
        self.home_page.click_on_like_button()
        self.assertTrue(self.home_page.check_like_button_activity())
        print("--------------------------------------------")

    # ------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()
