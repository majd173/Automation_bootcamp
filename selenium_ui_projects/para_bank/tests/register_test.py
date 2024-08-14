import unittest
import time
from selenium_ui_projects.para_bank.infra.config_provider import ConfigProvider
from selenium_ui_projects.para_bank.infra.browser_wrapper import BrowserWrapper
# from intro_to_selenium.para_bank.infra.utils import Utils
#tests
from selenium_ui_projects.para_bank.logic.home_page import HomePage
from selenium_ui_projects.para_bank.logic.register import Register
from selenium_ui_projects.para_bank.logic.register_successfully import RegisterSuccessfully
from selenium_ui_projects.para_bank.logic.registered_unsuccessfully import RegisterUsuccessfully

class TestRegister(unittest.TestCase):
    # testing register process class

    def setUp(self):
        self.config = ConfigProvider.load_from_file('../config.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)
    # opening the homepage before all tests

    def tearDown(self):
        self._driver.quit()
    # closing the web browser after every test

    def test_valid_register(self):
        print("valid register testing began...")
        self.home_page.go_to_register()
        register = Register(self._driver)
        register.valid_register_flow()
        confirm = RegisterSuccessfully(self._driver)
        confirm.confirm_message()
        self.assertTrue(confirm.confirm_message())
        time.sleep(2)
        print("-------------------------------------")
    # testing registering with valid details

    def test_invalid_register(self):
        self.home_page.go_to_register()
        register = Register(self._driver)
        register.invalid_register_flow()
        confirm = RegisterUsuccessfully(self._driver)
        confirm.register_failed()
        self.assertTrue(confirm.register_failed())
        time.sleep(2)
        print("-------------------------------------")
    # testing registering with invalid username but valid details





