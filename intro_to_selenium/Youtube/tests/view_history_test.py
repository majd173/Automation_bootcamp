import logging
import unittest
import time
from intro_to_selenium.para_bank.infra.config_provider import ConfigProvider
from intro_to_selenium.para_bank.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.Youtube.logic.home_page import HomePage
from intro_to_selenium.Youtube.logic.view_history import ViewHistoryAsCustomer


class TestViewHistory(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider.load_from_file('../../solarsystemscope/config.json')
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
