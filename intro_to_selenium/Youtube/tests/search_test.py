import time
import unittest
from intro_to_selenium.para_bank.infra.config_provider import ConfigProvider
from intro_to_selenium.para_bank.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.Youtube.logic.home_page import HomePage
from intro_to_selenium.Youtube.logic.search_submit import SearchSubmit



class TestSearchSubmit(unittest.TestCase):


    def setUp(self):
        self.config = ConfigProvider.load_from_file('../config.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)
    # opening the homepage before all tests

    def tearDown(self):
        self._driver.close()
    # closing the website after all tests

    def test_search_and_result_match(self):
        print("Search and result match testing began...")
        input = self.home_page.search_submit("Best of Michael Jordan")
        results_page = SearchSubmit(self._driver)
        result = results_page.search_and_confirm_result()
        self.assertIn(input, result, "True, search input appears in search result.")
        time.sleep(3) # In order to check if the search input inside the search result.
        print("--------------------------------------------")
        # Tests if a specific search input is included in the search result.

