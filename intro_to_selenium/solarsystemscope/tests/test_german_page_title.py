import unittest
from intro_to_selenium.solarsystemscope.infra.config_provider import ConfigProvider
from intro_to_selenium.solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.solarsystemscope.logic.home_page import HomePage
from intro_to_selenium.solarsystemscope.logic.german_page import GermanPage

class TestGermanPage(unittest.TestCase):



    def setUp(self):
        self.config = ConfigProvider.load_from_file('../config.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)
        # self.home_page.valid_log_in_flow()


    #opening the homepage before all tests

    def tearDown(self):
        self._driver.close()
    # closing the website after all tests


    def test_german_page_title_match(self):
        print("GERMAN WEBSITE ACTIVITY TESTING BEGAN...")
        self.home_page.click_on_german_page_button()
        german = GermanPage(self._driver)
        self.assertNotIn('Sonnensystem', german.get_page_title(self._driver), "ERROR, TITLES ARE THE SAME.")
        print("--------------------------------------------")


if __name__ == '__main__':
    unittest.main()