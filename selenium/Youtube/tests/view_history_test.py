import logging
import unittest
import time
from selenium.Youtube.infra.config_provider import ConfigProvider
from selenium.Youtube.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from selenium.Youtube.logic.home_page import HomePage
from selenium.Youtube.logic.view_history import ViewHistoryAsCustomer


class TestViewHistory(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider.load_from_file('../config.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)

    # opening the homepage before all tests

    def tearDown(self):
        self._driver.close()


    def test_view_history_as_customer(self):
        logging.info("view history as a customer test began")
        self.home_page.go_to_history()
        history = ViewHistoryAsCustomer(self._driver)
        history.return_error_message()
        self.assertTrue("Watch history isn't viewable when you're signed out.", history.return_error_message(), "Expected result is not correct")
        time.sleep(2)
        print("--------------------------------------------")
