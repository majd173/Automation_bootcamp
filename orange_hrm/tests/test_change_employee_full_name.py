import unittest
#-----------------------------API CLASSES----------------------------
from orange_hrm.api.logic.my_info_page import ApiMyInfoPage
from orange_hrm.api.infra.api_wrapper import ApiWrapper
from orange_hrm.api.infra.config_provider import ConfigProvider
from orange_hrm.api.infra.utilities import Utils
from orange_hrm.preson_object import PersonObject
#-----------------------------UI CLASSES-----------------------------
from orange_hrm.ui.logic.log_in_page import LogInPage
from orange_hrm.ui.logic.home_page import HomePage
from orange_hrm.ui.logic.my_info_page import UiMyInfoPage
from orange_hrm.ui.infra.config_provider import ConfigProvider
from orange_hrm.ui.infra.browser_wrapper import BrowserWrapper


class TestOrangeHrm(unittest.TestCase):

    def tearDown(self):
        # self._api_info_page.retrieve_employee_full_name()
        self._driver.close()

    def test_changing_employee_fullname(self):
        self._config = ConfigProvider().load_from_file(r'/orange_hrm/orange_hrm.json')
        self._driver = BrowserWrapper().get_driver()
        self._login_page = LogInPage(self._driver)
        token = self._login_page.login_flow()
        self._api = ApiWrapper()
        self._api_info_page = ApiMyInfoPage(self._api)
        person_object = PersonObject(Utils.generate_random_string_only_letters(5).lower(),
                                     Utils.generate_random_string_only_letters(5).lower(),
                                     Utils.generate_random_string_only_letters(5).lower())
        self._api_info_page.change_employee_full_name(token, person_object)
        home_page = HomePage(self._driver)
        home_page.refresh_page()
        self.assertEqual(home_page.get_full_name()[0], person_object.first_name)
        self.assertEqual(home_page.get_full_name()[1], person_object.last_name)




if __name__ == '__main__':
    unittest.main()
