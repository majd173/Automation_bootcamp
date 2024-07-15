import unittest
import logging
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
        self.home_page.valid_log_in_flow()

    # ------------------------------------------------------------------------------------------------------------
    # This function closes the website after all tests.
    def tearDown(self):
        self._driver.close()
        logging.info(f'{self.config["browser"]} browser was closed.'
        f'\n-------------------------------------------------------')


    # ------------------------------------------------------------------------------------------------------------
    # Testing integration and switching to Eretz Museum website.
    # Test case no: 10 - To ensure that a customer can integrate
    # with another website through SolarSystemScope website.

    def test_eretz_museum_page(self):
        logging.info("_____ERETZ MUSEUM URL MATCH TESTING BEGAN_____")
        current_window = self._driver.current_window_handle
        self.home_page.click_on_explore()
        self.home_page.click_on_astronomy_places()
        astronomy_places = AstronomyPlacesPage(self._driver)
        astronomy_places.click_on_load_places()
        astronomy_places.window_switch(current_window)
        eretz_museum = EretzMuseumPage(self._driver)
        self._driver.save_screenshot('After Opening Eretz museum website.png')
        self.assertIn("eretzmuseum", eretz_museum.get_current_url(),
        "THE CURRENT URL IS NOT AS EXPECTED.")
        logging.info("----------------- TEST DONE ------------------")


if __name__ == '__main__':
    unittest.main()
