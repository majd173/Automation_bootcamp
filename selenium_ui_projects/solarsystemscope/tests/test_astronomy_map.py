import unittest
import logging
# tests ---------------------------------infra----------------------------------------files
from selenium_ui_projects.solarsystemscope.infra.config_provider import ConfigProvider
from selenium_ui_projects.solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from selenium_ui_projects.solarsystemscope.logic.home_page import HomePage
from selenium_ui_projects.solarsystemscope.logic.astronomy_places import AstronomyPlacesPage

class TestAstronomyPlacesMap(unittest.TestCase):


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
    # Testing the display of astronomy places map.
    # Test case no: 3 - To ensure that a customer can preview astronomy places map.


    def test_astronomy_places_map_display(self):
        logging.info("_____ASTRONOMY PLACES MAP DISPLAY TESTING BEGAN_____")
        logging.info(f'{self.config["browser"]} browser was opened')
        self.home_page.click_on_explore()
        self.home_page.click_on_astronomy_places()
        map = AstronomyPlacesPage(self._driver)
        self.assertTrue(map.map_display(), "ASTRONOMY PLACES MAP display error.")

if __name__ == '__main__':
    unittest.main()
