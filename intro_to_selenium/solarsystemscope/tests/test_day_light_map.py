import unittest
from intro_to_selenium.solarsystemscope.infra.config_provider import ConfigProvider
from intro_to_selenium.solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.solarsystemscope.logic.home_page import HomePage
from intro_to_selenium.solarsystemscope.logic.online_apps_page import OnlineAppsPage
from intro_to_selenium.solarsystemscope.logic.day_light_map_page import DayLightMapPage


class TestDayLightMap(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider.load_from_file('../config.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)
        # self.home_page.valid_log_in_flow()

    #opening the homepage before all tests

    def tearDown(self):
        self._driver.close()

    # closing the website after all tests


    def test_adobe_request_message(self):
        print("ADOBE FLASH REQUEST MESSAGE DISPLAY TESTING BEGAN...")
        self.home_page.click_on_explore()
        self.home_page.click_on_online_apps_button()
        online_apps_page = OnlineAppsPage(self._driver)
        online_apps_page.click_on_day_light_map_button()
        day_light_map_page = DayLightMapPage(self._driver)
        self.assertEqual("Adobe Flash", day_light_map_page.adobe_request_message_display(),
                      "ADOBE REQUEST IS NOT DISPLAYED.")
        print("--------------------------------------------")


