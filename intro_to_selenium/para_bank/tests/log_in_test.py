import unittest
import time
from intro_to_selenium.para_bank.infra.config_provider import ConfigProvider
from intro_to_selenium.para_bank.infra.browser_wrapper import BrowserWrapper
#tests
from intro_to_selenium.para_bank.logic.home_page import HomePage
from intro_to_selenium.para_bank.logic.log_in_successfully import LogInSuccessfully
from intro_to_selenium.para_bank.logic.log_in_unsuccessfully import LogInUnsuccessfully

class TestLogIn(unittest.TestCase):


    def setUp(self):
        self.config = ConfigProvider.load_from_file('../config.json')
        self.driver = BrowserWrapper().get_driver(self.config["base_url"])
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_valid_log_in(self):
        print("valid log_in testing began...")
        self.home_page.valid_login_flow('111', '111')
        log_in_successfully = LogInSuccessfully(self.driver)
        log_in_successfully.confirm_table()
        time.sleep(2)
        print("-------------------------------------")


    def test_invalid_log_in(self):
        print("invalid log_in testing began...")
        self.home_page.invalid_log_in_flow()
        log_in_unsuccessfully = LogInUnsuccessfully(self.driver)
        log_in_unsuccessfully.log_in_failed()
        time.sleep(2)
        print("-------------------------------------")


