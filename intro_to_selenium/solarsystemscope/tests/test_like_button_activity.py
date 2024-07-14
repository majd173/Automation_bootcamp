import logging
import unittest
# tests ---------------------------------infra----------------------------------------files
from intro_to_selenium.solarsystemscope.infra.config_provider import ConfigProvider
from intro_to_selenium.solarsystemscope.infra.browser_wrapper import BrowserWrapper
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
        logging.info(f'{self.config["browser"]} browser was closed.\n--------------------------------------------')


    # ------------------------------------------------------------------------------------------------------------

    def test_like_button_activity(self):
        logging.info("LIKE BUTTON ACTIVITY TESTING BEGAN...")
        self.home_page.click_on_like_button()
        self.assertTrue(self.home_page.check_like_button_activity())
        print("---------------------- TEST DONE -----------------------")



if __name__ == '__main__':
    unittest.main()
