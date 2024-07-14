import unittest
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# tests ---------------------------------infra----------------------------------------files
from intro_to_selenium.solarsystemscope.infra.config_provider import ConfigProvider
from intro_to_selenium.solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.solarsystemscope.logic.home_page import HomePage
from intro_to_selenium.solarsystemscope.logic.astronomy_places import AstronomyPlacesPage
from intro_to_selenium.solarsystemscope.logic.eretz_museum_page import EretzMuseumPage


class TestEretzMuseumPage(unittest.TestCase):

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

    def test_eretz_museum_page(self):
        logging.info("ERETZ MUSEUM URL MATCH TESTING BEGAN...")
        original_window = self._driver.current_window_handle
        self.home_page.click_on_explore()
        self.home_page.click_on_astronomy_places()
        astronomy_places = AstronomyPlacesPage(self._driver)
        astronomy_places.click_on_load_places()
        assert len(self._driver.window_handles) == 1
        astronomy_places.click_on_eretz_museum_button()
        WebDriverWait(self._driver, 10).until(EC.number_of_windows_to_be(2))
        for window_handle in self._driver.window_handles:
            if window_handle != original_window:
                self._driver.switch_to.window(window_handle)
                break
        eretz_museum = EretzMuseumPage(self._driver)
        self._driver.save_screenshot('After clicking Eretz museum button and opening Eretz Museum website.png')
        self.assertIn("eretzmuseum", eretz_museum.get_page_url(),
                      "THE CURRENT URL IS NOT AS EXPECTED.")
        print("---------------------- TEST DONE -----------------------")


if __name__ == '__main__':
    unittest.main()
