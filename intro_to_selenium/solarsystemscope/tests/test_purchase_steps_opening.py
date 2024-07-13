import logging
import unittest
import unittest
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

    # ------------------------------------------------------------------------------------------------------------

    def test_purchase_steps_opening(self):
        logging.info("PURCHASE STEPS OPENING TESTING BEGAN...")
        self.home_page.click_on_download_app()
        download = DownloadAppPage(self._driver)
        download.click_on_show_button()
        self.assertTrue(download.purchase_steps_opening(), "PURCHASE STEPS IS NOT OPENED.")
        print("--------------------------------------------")


    # ------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()
