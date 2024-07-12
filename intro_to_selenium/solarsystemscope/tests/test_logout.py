import unittest
from intro_to_selenium.solarsystemscope.infra.config_provider import ConfigProvider
from intro_to_selenium.solarsystemscope.infra.browser_wrapper import BrowserWrapper
# tests ---------------------------------logic----------------------------------------files
from intro_to_selenium.solarsystemscope.logic.home_page import HomePage


class TestLogout(unittest.TestCase):

    # ------------------------------------------------------------------------------------------------------------
    # This function opens the homepage before all tests.
    def setUp(self):
        self.config = ConfigProvider.load_from_file('../config.json')
        self._driver = BrowserWrapper().get_driver()
        self.home_page = HomePage(self._driver)
        self.home_page.valid_log_in_flow()

    # ------------------------------------------------------------------------------------------------------------
    # This function closes the website after all tests.

    def tearDown(self):
        self._driver.close()

    # ------------------------------------------------------------------------------------------------------------

    def test_logout_successfully(self):
        print("LOGOUT SUCCESSFULLY TESTING BEGAN...")
        self.home_page.click_on_logout_button()
        self.assertTrue(self.home_page.logout_confirmation())
        print("--------------------------------------------")

    # ------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()