import logging
import unittest
# tests ---------------------------------infra----------------------------------------files
from selenium_ui_projects.solarsystemscope.infra.config_provider import ConfigProvider
from selenium_ui_projects.solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from selenium_ui_projects.solarsystemscope.logic.home_page import HomePage
from selenium_ui_projects.solarsystemscope.logic.astronomy_places import AstronomyPlacesPage


class TestDistantPlacesList(unittest.TestCase):

    # ------------------------------------------------------------------------------------------------------------
    # This function opens the homepage before all tests.

    def setUp(self):
        self.config = ConfigProvider.load_from_file('../solar_config.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)
        # self.home_page.valid_log_in_flow()
    # ------------------------------------------------------------------------------------------------------------

    def tearDown(self):
        self._driver.close()
        logging.info(f'{self.config["browser"]} browser was closed.')
        logging.info("----------------- TEST DONE ------------------\n")


    # ------------------------------------------------------------------------------------------------------------
    # Testing activity of opening distant places list.
    # Test case no: 6 - To ensure that a customer can open the Distant Places list.
    def test_open_distant_places_list(self):
        logging.info("_____OPEN DISTANT PLACES LIST TESTING BEGAN_____")
        logging.info(f'{self.config["browser"]} browser was opened')
        self.home_page.click_on_explore()
        self.home_page.click_on_astronomy_places()
        astronomy_places = AstronomyPlacesPage(self._driver)
        astronomy_places.click_on_load_places()
        self.assertTrue(astronomy_places.display_added_box(), "ADDED BOX can not be displayed.")


if __name__ == '__main__':
    unittest.main()