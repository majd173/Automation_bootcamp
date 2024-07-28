import unittest
import logging
# tests ---------------------------------infra----------------------------------------files
from selenium_projects.solarsystemscope.infra.config_provider import ConfigProvider
from selenium_projects.solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from selenium_projects.solarsystemscope.logic.home_page import HomePage
from selenium_projects.solarsystemscope.logic.astronomy_places import AstronomyPlacesPage
from selenium_projects.solarsystemscope.logic.eretz_museum_page import EretzMuseumPage

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

    def test_eretz_museum_dot_click(self):
        logging.info("_____ERETZ MUSEUM DOTS CLICK TESTING BEGAN_____")
        logging.info(f'{self.config["browser"]} browser was opened')
        current_window = self._driver.current_window_handle
        self.home_page.click_on_explore()
        self.home_page.click_on_astronomy_places()
        astronomy_places = AstronomyPlacesPage(self._driver)
        astronomy_places.click_on_load_places()
        astronomy_places.window_switch(current_window)
        eretz_museum = EretzMuseumPage(self._driver)
        eretz_museum.click_on_dots()
        self.assertTrue(eretz_museum.check_dot_clickable())



if __name__ == '__main__':
    unittest.main()
