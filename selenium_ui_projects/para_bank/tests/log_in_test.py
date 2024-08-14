import unittest
import time
from selenium_ui_projects.para_bank.infra.config_provider import ConfigProvider
from selenium_ui_projects.para_bank.infra.browser_wrapper import BrowserWrapper
#tests
from selenium_ui_projects.para_bank.logic.home_page import HomePage
from selenium_ui_projects.para_bank.logic.log_in_successfully import LogInSuccessfully
from selenium_ui_projects.para_bank.logic.log_in_unsuccessfully import LogInUnsuccessfully

class TestLogIn(unittest.TestCase):
    # testing logging in class

    def setUp(self):
        self.config = ConfigProvider.load_from_file('../config.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)
    # opening the homepage before all tests
    def tearDown(self):
        self._driver.quit()
    # closing the web browser after every test

    def test_valid_log_in(self):
        print("valid log_in testing began...")
        self.home_page.valid_login_flow('111', '111')
        log_in_successfully = LogInSuccessfully(self._driver)
        log_in_successfully.confirm_table()
        self.assertTrue(log_in_successfully.confirm_table())
        time.sleep(2)
        print("-------------------------------------")
        # testing logging in using valid username and valid password

    def test_invalid_log_in(self):
        print("invalid log_in testing began...")
        self.home_page.invalid_log_in_flow()
        log_in_unsuccessfully = LogInUnsuccessfully(self._driver)
        log_in_unsuccessfully.log_in_failed()
        self.assertTrue(log_in_unsuccessfully.log_in_failed())
        time.sleep(2)
        print("-------------------------------------")
        # testing invalid logging in using no username and valid password

