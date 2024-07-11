import unittest
from intro_to_selenium.solarsystemscope.infra.config_provider import ConfigProvider
from intro_to_selenium.solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.solarsystemscope.logic.home_page import HomePage
from intro_to_selenium.solarsystemscope.logic.download_app_page import DownloadApp



class TestAppFeaturesPreview(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider.load_from_file('../config.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)
        # self.home_page.valid_log_in_flow()


    #opening the homepage before all tests

    def tearDown(self):
        self._driver.close()
    # closing the website after all tests


    def test_app_fueature_preview(self):
        print("APP FEATURES PREVIEW TESTING BEGAN...")
        self.home_page.click_on_download_app()
        download = DownloadApp(self._driver)
        download.click_preview_button()
        self.assertTrue(download.earth_image_display(),"APP FEATURES DISPLAY ERROR.")
        print("--------------------------------------------")
