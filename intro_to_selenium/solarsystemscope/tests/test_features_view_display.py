import logging
import unittest
# tests ---------------------------------infra----------------------------------------files
from intro_to_selenium.solarsystemscope.infra.config_provider import ConfigProvider
from intro_to_selenium.solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.solarsystemscope.logic.home_page import HomePage
from intro_to_selenium.solarsystemscope.logic.download_app_page import DownloadAppPage



class TestAppFeaturesPreview(unittest.TestCase):

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
        logging.info("----------------- TEST DONE ------------------\n"
                     "---------------------------------------------------------------------------")


    # ------------------------------------------------------------------------------------------------------------
    # Testing the preview of the app features.
    # Test case no: 4 - To ensure that a customer can view features of desktop app.


    def test_app_features_preview(self):
        logging.info("_____APP FEATURES PREVIEW TESTING BEGAN_____")
        logging.info(f'{self.config["browser"]} browser was opened')
        self.home_page.click_on_download_app()
        download = DownloadAppPage(self._driver)
        download.click_preview_button()
        self.assertTrue(download.earth_image_display(),"APP FEATURES display error.")


if __name__ == '__main__':
    unittest.main()