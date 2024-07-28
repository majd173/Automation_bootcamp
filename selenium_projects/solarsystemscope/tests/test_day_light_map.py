import unittest
import logging
# tests ---------------------------------infra----------------------------------------files
from selenium_projects.solarsystemscope.infra.config_provider import ConfigProvider
from selenium_projects.solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from selenium_projects.solarsystemscope.logic.home_page import HomePage
from selenium_projects.solarsystemscope.logic.online_apps_page import OnlineAppsPage
from selenium_projects.solarsystemscope.logic.day_light_map_page import DayLightMapPage


class TestDayLightMap(unittest.TestCase):

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
    # Testing display of Adobe request message.
    # Test case no: 5 - To ensure that a customer can not run online maps without Adobe flash exist.

    def test_adobe_request_message(self):
        logging.info("_____ADOBE FLASH REQUEST MESSAGE DISPLAY TESTING BEGAN_____")
        logging.info(f'{self.config["browser"]} browser was opened')
        self.home_page.click_on_explore()
        self.home_page.click_on_online_apps_button()
        online_apps_page = OnlineAppsPage(self._driver)
        online_apps_page.click_on_day_light_map_button()
        day_light_map_page = DayLightMapPage(self._driver)
        self.assertEqual("Adobe Flash", day_light_map_page.adobe_request_message_display(),
        "ADOBE REQUEST is not displayed.")


if __name__ == '__main__':
    unittest.main()
