import unittest
from intro_to_selenium.solarsystemscope.infra.config_provider import ConfigProvider
from intro_to_selenium.solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.solarsystemscope.logic.home_page import HomePage
from intro_to_selenium.solarsystemscope.logic.online_store_page import OnlineStorePage
from intro_to_selenium.solarsystemscope.logic.organic_products_page import OrganicProductsPage


class TestOrganicProductsPage(unittest.TestCase):

    def setUp(self):
        self.config = ConfigProvider.load_from_file('../config.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)
        # self.home_page.valid_log_in_flow()

    #opening the homepage before all tests

    def tearDown(self):
        self._driver.close()

    # closing the website after all tests


    def test_organic_products_page(self):
        print("ORGANIC PRODUCTS PAGE DISPLAY TESTING BEGAN...")
        self.home_page.click_on_explore()
        self.home_page.click_on_merchandise_button()
        online_store_page = OnlineStorePage(self._driver)
        online_store_page.hover_on_men_tab()
        organic_products_page = OrganicProductsPage(self._driver)
        self.assertEqual(organic_products_page.header_title_display(),
                         "Men - Organic Products", "ORGANIC PRODUCTS HEADER TITLE IS WRONG.")
