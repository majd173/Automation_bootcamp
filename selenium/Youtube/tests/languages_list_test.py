import logging
import unittest
import time
from selenium.Youtube.infra.config_provider import ConfigProvider
from selenium.Youtube.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from selenium.Youtube.logic.home_page import HomePage
from selenium.Youtube.logic.languages import LanguageList


class TestLanguagesList(unittest.TestCase):


    def setUp(self):
        self.config = ConfigProvider.load_from_file('../config.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)

    # opening the homepage before all tests

    def tearDown(self):
        self._driver.close()
    # closing the website after all tests

    def test_languages_list_display(self):
        print("Checking languages list display test began...")
        self.home_page.open_languages_list()
        languages_list = LanguageList(self._driver)
        self.assertEqual(languages_list.confirm_languages_pop_up_window(), True)
        time.sleep(3) # In order to confirm display of languages list.
        print("--------------------------------------------")
        # Tests display of languages list.



