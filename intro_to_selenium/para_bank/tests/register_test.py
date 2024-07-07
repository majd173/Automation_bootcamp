import unittest
import time
from intro_to_selenium.para_bank.infra.config_provider import ConfigProvider
from intro_to_selenium.para_bank.infra.browser_wrapper import BrowserWrapper
# from intro_to_selenium.para_bank.infra.utils import Utils
#tests
from intro_to_selenium.para_bank.logic.home_page import HomePage
from intro_to_selenium.para_bank.logic.register import Register
from intro_to_selenium.para_bank.logic.register_successfully import RegisterSuccessfully
from intro_to_selenium.para_bank.logic.registered_unsuccessfully import RegisterUsuccessfully

class TestRegister(unittest.TestCase):


    def setUp(self):
        self.config = ConfigProvider.load_from_file('../config.json')
        self.driver = BrowserWrapper().get_driver(self.config["base_url"])
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_valid_register(self):
        print("valid register testing began...")
        self.home_page.go_to_register()
        register = Register(self.driver)
        register.valid_register_flow()
        confirm = RegisterSuccessfully(self.driver)
        confirm.confirm_message()
        time.sleep(2)
        print("-------------------------------------")


    def test_invalid_register(self):
        self.home_page.go_to_register()
        register = Register(self.driver)
        register.invalid_register_flow()
        confirm = RegisterUsuccessfully(self.driver)
        confirm.register_failed()
        time.sleep(2)
        print("-------------------------------------")





