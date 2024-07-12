import unittest
from intro_to_selenium.firefox_solarsystemscope.infra.config_provider import ConfigProvider
from intro_to_selenium.firefox_solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.firefox_solarsystemscope.logic.home_page import HomePage
from intro_to_selenium.firefox_solarsystemscope.logic.download_app_page import DownloadAppPage



class TestAppFeaturesPreview(unittest.TestCase):

    # ------------------------------------------------------------------------------------------------------------
    # This function opens the homepage before all tests.
    def setUp(self):
        self.config = ConfigProvider.load_from_file('../config_firefox.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)
        # self.home_page.valid_log_in_flow()

    # ------------------------------------------------------------------------------------------------------------
    # This function closes the website after all tests.
    def tearDown(self):
        self._driver.close()

    # ------------------------------------------------------------------------------------------------------------

    def test_app_features_preview(self):
        print("APP FEATURES PREVIEW TESTING BEGAN...")
        self.home_page.click_on_download_app()
        download = DownloadAppPage(self._driver)
        download.click_preview_button()
        self.assertTrue(download.earth_image_display(),"APP FEATURES DISPLAY ERROR.")
        print("--------------------------------------------")

if __name__ == '__main__':
    unittest.main()