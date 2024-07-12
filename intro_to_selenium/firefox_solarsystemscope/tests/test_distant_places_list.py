import unittest
from intro_to_selenium.firefox_solarsystemscope.infra.config_provider import ConfigProvider
from intro_to_selenium.firefox_solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.firefox_solarsystemscope.logic.home_page import HomePage
from intro_to_selenium.firefox_solarsystemscope.logic.astronomy_places import AstronomyPlacesPage


class TestDistantPlacesList(unittest.TestCase):

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

    def test_open_distant_places_list(self):
        print("OPEN DISTANT PLACES LIST TESTING BEGAN...")
        self.home_page.click_on_explore()
        self.home_page.click_on_astronomy_places()
        astronomy_places = AstronomyPlacesPage(self._driver)
        astronomy_places.click_on_load_places()
        self.assertTrue(astronomy_places.display_added_box(), "ADDED BOX CAN NOT BE DISPLAYED.")
        print("--------------------------------------------")


if __name__ == '__main__':
    unittest.main()