import unittest
from orange_hrm.api.logic.my_info_page import ApiMyInfoPage
from orange_hrm.api.api_wrapper import ApiWrapper
from orange_hrm.api.config_provider import ConfigProvider

from orange_hrm.ui.logic.log_in_page import LogInPage
from orange_hrm.ui.logic.home_page import HomePage
from orange_hrm.ui.logic.my_info_page import UiMyInfoPage
from orange_hrm.ui.config_provider import ConfigProvider
from orange_hrm.ui.browser_wrapper import BrowserWrapper


class TestOrangeHrm(unittest.TestCase):

    def setUp(self):
        self._config = ConfigProvider().load_from_file(r'C:\Users\Admin\Desktop\Automation_bootcamp\orange_hrm\orange_hrm.json')
        self._api = ApiWrapper()
        self._api_info_page = ApiMyInfoPage(self._api)
        self._driver = BrowserWrapper().get_driver()
        self._login_page = LogInPage(self._driver)
        self._home_page = HomePage(self._driver)
        self._ui_info_page = UiMyInfoPage(self._driver)
        # ACT
        self._login_page.login_flow()

    def tearDown(self):

        self._driver.close()


    def test_changing_employee_fullname(self):
        self._home_page.click_on_my_info()
        self._response = self._api_info_page.change_employee_full_name()
        self._ui_info_page.refresh_page()
        self.assertEqual(200, self._response.status_code)
        self.assertTrue(self._ui_info_page.check_employee_full_name())





if __name__ == '__main__':
    unittest.main()
