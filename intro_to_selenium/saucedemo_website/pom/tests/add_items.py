import unittest
from selenium import webdriver
from intro_to_selenium.saucedemo_website.pom.infra.config_provider import ConfigProvider
from intro_to_selenium.saucedemo_website.pom.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.saucedemo_website.pom.logic.main import Main
from intro_to_selenium.saucedemo_website.pom.logic.log_in import TestLogIn
from intro_to_selenium.saucedemo_website.pom.logic.cart import Cart
from intro_to_selenium.saucedemo_website.pom.logic.logged_in_successfully_page import LoggedInSuccessfully
import time


class TestAddItems(unittest.TestCase):

    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(12)
    #     self.driver.maximize_window()
    #
    # def tearDown(self):
    #     self.driver.quit()
    def test_login_successfully(self):
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        print("log in test")
        # driver.maximize_window()
        driver.implicitly_wait(12)
        # self.driver.get('https://www.saucedemo.com/inventory.html')
        login_page = TestLogIn(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        cart_page = LoggedInSuccessfully(driver)
        result = cart_page.menu_is_exist()
        self.assertTrue(result, 'True')
        print(f'{result}, menu button exists after logging in, you are in the main page')
        print("---------------------------------")
        driver.quit()



    def test_add_two_items(self):

        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        print("adding two items to the cart test")
        driver.implicitly_wait(12)
        # driver.maximize_window()
        login_page = TestLogIn(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        cart_page = LoggedInSuccessfully(driver)
        result = cart_page.menu_is_exist()
        print(f'{result}, menu button exists after logging in, you are in the main page')
        self.assertTrue(result, 'True')
        item = Main(driver)
        item.click_sauce_back_pack()
        item.click_sauce_labs_bike_light()
        item.test_go_to_cart()
        # item2 = Cart(driver)
        # item2.check_items_exist()
        print("---------------------------------")
        driver.quit()


    def test_add_three_items(self):
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        print("adding three items to the cart and removing one item...")
        driver.implicitly_wait(10)
        # driver.maximize_window()
        login_page = TestLogIn(driver)
        login_page.login_flow("standard_user", "secret_sauce")
        cart_page = LoggedInSuccessfully(driver)
        result = cart_page.menu_is_exist()
        print(f'{result}, menu button exists after logging in, you are in the main page')
        self.assertTrue(result, 'True')
        item = Main(driver)
        item.click_sauce_back_pack()
        item.click_sauce_labs_bike_light()
        item.click_sauce_labs_bolt_t_shirt()
        item.test_go_to_cart()
        item2 = Cart(driver)
        item2.remove_item("//button[@id = 'remove-sauce-labs-bolt-t-shirt']")
        item2.check_items_exist()
        print("---------------------------------")

        driver.quit()



if __name__ == '__main__':
    unittest.main()
