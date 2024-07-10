import unittest
from intro_to_selenium.solarsystemscope.infra.config_provider import ConfigProvider
from intro_to_selenium.solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.solarsystemscope.logic.home_page import HomePage
from intro_to_selenium.solarsystemscope.logic.astronomy_places import AstronomyPlaces


class TestAstronomyPlacesMap(unittest.TestCase):


    def setUp(self):
        self.config = ConfigProvider.load_from_file('../config.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)
        self.home_page.valid_log_in_flow()

    #opening the homepage before all tests

    def tearDown(self):
        self._driver.close()

    # closing the website after all tests


    def test_astronomy_places_map_display(self):
        print("ASTRONOMY PLACES MAP DISPLAY TESTING BEGAN...")
        self.home_page.click_on_explore()
        self.home_page.click_on_astronomy_places()
        map = AstronomyPlaces(self._driver)
        self.assertTrue(map.map_display(), "ASTRONOMY PLACES MAP DISPLAY ERROR.")
        print("--------------------------------------------")
