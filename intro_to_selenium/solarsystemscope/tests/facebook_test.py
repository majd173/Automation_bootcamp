import logging
import time
import unittest
from intro_to_selenium.solarsystemscope.infra.config_provider import ConfigProvider
from intro_to_selenium.solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.solarsystemscope.logic.home_page import HomePage
from intro_to_selenium.solarsystemscope.logic.facebook_page import FcebookPage



class TestFacebookIntegration(unittest.TestCase):


    def setUp(self):
        self.config = ConfigProvider.load_from_file('../config.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)
        self.home_page.valid_log_in_flow()

    #opening the homepage before all tests

    def tearDown(self):
        self._driver.close()
    # closing the website after all tests

    def test_facebook_integration(self):
        print("FACEBOOK WEBSITE INTEGRATION TESTING BEGAN...")
        self.home_page.click_on_facebook()
        facebook = FcebookPage(self._driver)
        self.assertEqual(facebook.website_title_match(self._driver), "Solar System Scope - Online Model of Solar System and Night Sky", "TITLE IS NOT CORRECT.")
        print("--------------------------------------------")
