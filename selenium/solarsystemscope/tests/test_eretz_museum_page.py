import unittest
import logging
# tests ---------------------------------infra----------------------------------------files
from selenium.solarsystemscope.infra.config_provider import ConfigProvider
from selenium.solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from selenium.solarsystemscope.logic.home_page import HomePage
from selenium.solarsystemscope.logic.astronomy_places import AstronomyPlacesPage


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
        logging.info(f'{self.config["browser"]} browser was closed.')
        logging.info("----------------- TEST DONE ------------------\n")

    # ------------------------------------------------------------------------------------------------------------
    # Testing integration and switching to Eretz Museum website.
    # Test case no: 10 - To ensure that a customer can integrate
    # with another website through SolarSystemScope website.

    def test_eretz_museum_page(self):
        logging.info("_____ERETZ MUSEUM URL MATCH TESTING BEGAN_____")
        logging.info(f'{self.config["browser"]} browser was opened')
        current_window = self._driver.current_window_handle
        self.home_page.click_on_explore()
        self.home_page.click_on_astronomy_places()
        astronomy_places = AstronomyPlacesPage(self._driver)
        astronomy_places.click_on_load_places()
        astronomy_places.window_switch(current_window)
        self.assertIn("eretzmuseum", self._driver.current_url,
                      "The current url is not as expected.")



if __name__ == '__main__':
    unittest.main()
