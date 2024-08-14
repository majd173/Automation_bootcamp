import time
import unittest
from selenium_ui_projects.the_internet_herokuapp.infra.config_provider import ConfigProvider
from selenium_ui_projects.the_internet_herokuapp.infra.browser_wrapper import BrowserWrapper
from selenium_ui_projects.the_internet_herokuapp.logic.home_page import HomePage
# Tests
from selenium_ui_projects.the_internet_herokuapp.logic.second_6.drop_down import DropDown
from selenium_ui_projects.the_internet_herokuapp.logic.second_6.dynamic_content import DynamicContent
from selenium_ui_projects.the_internet_herokuapp.logic.second_6.dynamic_controls import DynamicControls
from selenium_ui_projects.the_internet_herokuapp.logic.second_6.file_download import FileDownload
from selenium_ui_projects.the_internet_herokuapp.logic.second_6.file_upload import FileUpload
from selenium_ui_projects.the_internet_herokuapp.logic.second_6.floating_menu import FloatingMen


class TestSiteTwo(unittest.TestCase):

    def test_drop_down_choose_options(self):
        print("Test no: 7")
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        home_page = HomePage(driver)
        drop_down_url = home_page.get_link(10)
        driver.get(drop_down_url)
        drop_down_element = DropDown(driver)
        time.sleep(1)
        drop_down_element.drop_down()
        time.sleep(2)
        drop_down_element.click_option_1()
        time.sleep(2)
        drop_down_element.click_option_2()
        time.sleep(2)
        driver.quit()
        print("---------------------------------")

    def test_dynamic_content(self):
        print("Test no: 8")
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        home_page = HomePage(driver)
        dynamic_content = home_page.get_link(11)
        driver.get(dynamic_content)
        dynamic_content_page = DynamicContent(driver)
        time.sleep(1)
        dynamic_content_page.change_content()
        time.sleep(2)
        driver.quit()
        print("---------------------------------")

    def test_dynamic_controls(self):
        print("Test no: 9")
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        home_page = HomePage(driver)
        dynamic_controls = home_page.get_link(12)
        driver.get(dynamic_controls)
        dynamic_controls_page = DynamicControls(driver)
        dynamic_controls_page.enable_text_bar()
        time.sleep(7)
        driver.quit()
        print("---------------------------------")

    def test_file_download(self):
        print("Test no: 10")
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        home_page = HomePage(driver)
        file_download_url = home_page.get_link(16)
        driver.get(file_download_url)
        file_download = FileDownload(driver)
        file_download.download_file()
        time.sleep(2)
        driver.quit()
        print("---------------------------------")


    # does not work
    def test_file_upload(self):
        print("Test no: 11")
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        home_page = HomePage(driver)
        file_upload_url = home_page.get_link(17)
        driver.get(file_upload_url)
        file_upload = FileUpload(driver)
        file_upload.upload_file()
        time.sleep(2)
        driver.quit()
        print("---------------------------------")

    def test_floating_menu(self):
        print("Test no: 12")
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        home_page = HomePage(driver)
        floating_menu_url = home_page.get_link(18)
        driver.get(floating_menu_url)
        floating_menu = FloatingMen(driver)
        floating_menu.scroll_down()
        time.sleep(2)
        driver.quit()
        print("---------------------------------")

if __name__ == '__main__':
    unittest.main()
