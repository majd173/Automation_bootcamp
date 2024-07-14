import logging
import unittest
# tests ---------------------------------infra----------------------------------------files
from intro_to_selenium.solarsystemscope.infra.config_provider import ConfigProvider
from intro_to_selenium.solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.solarsystemscope.logic.home_page import HomePage
from intro_to_selenium.solarsystemscope.logic.download_app_page import DownloadAppPage


class TestPurchaseStepsOpening(unittest.TestCase):

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
        logging.info(f'{self.config["browser"]} browser was closed.'
                     f'\n--------------------------------------------')

    # ------------------------------------------------------------------------------------------------------------
    # Testing activity of opening purchase steps tab.
    # Test case no: 9 - To ensure that a customer can open Purchase steps tab.

    def test_purchase_steps_opening(self):
        logging.info("_____PURCHASE STEPS OPENING TESTING BEGAN_____")
        self.home_page.click_on_download_app()
        download = DownloadAppPage(self._driver)
        download.click_on_show_button()
        self.assertTrue(download.purchase_steps_opening(), "PURCHASE STEPS IS NOT OPENED.")
        print("---------------------- TEST DONE -----------------------")



if __name__ == '__main__':
    unittest.main()
