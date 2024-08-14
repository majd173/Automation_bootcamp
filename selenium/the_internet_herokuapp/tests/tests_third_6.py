import time
import unittest
from selenium.the_internet_herokuapp.infra.config_provider import ConfigProvider
from selenium.the_internet_herokuapp.infra.browser_wrapper import BrowserWrapper
from selenium.the_internet_herokuapp.logic.home_page import HomePage
#tests
from selenium.the_internet_herokuapp.logic.third_6.horizontal_slider import HorizontalSlider
from selenium.the_internet_herokuapp.logic.third_6.hovers import Hovers
from selenium.the_internet_herokuapp.logic.third_6.infinite_scroll import InfiniteScroll
from selenium.the_internet_herokuapp.logic.third_6.ui_menu import UiMenu
from selenium.the_internet_herokuapp.logic.third_6.java_alerts import JavaAlerts
from selenium.the_internet_herokuapp.logic.third_6.data_tables import DataTables


class TestSite(unittest.TestCase):

    def test_horizontal_slider(self):
        print("Test no: 13")
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        home_page = HomePage(driver)
        horizontal_slider_url = home_page.get_link(23)
        driver.get(horizontal_slider_url)
        horizontal_slider = HorizontalSlider(driver)
        time.sleep(1)
        horizontal_slider.move_slider()
        time.sleep(2)
        print("---------------------------------")
        driver.quit()

    def test_hovers(self):
        print("Test no: 14")
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        home_page = HomePage(driver)
        hovers_url = home_page.get_link(24)
        driver.get(hovers_url)
        hovers = Hovers(driver)
        time.sleep(1)
        hovers.show_details()
        time.sleep(2)
        print("---------------------------------")
        driver.quit()

    def test_infinite_scroll(self):
        print("Test no: 15")
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        home_page = HomePage(driver)
        infinite_scroll_url = home_page.get_link(25)
        driver.get(infinite_scroll_url)
        infinite_scroll = InfiniteScroll(driver)
        time.sleep(1)
        infinite_scroll.infinite_scroll()
        time.sleep(2)
        print("---------------------------------")
        driver.quit()

    def test_ui_menu(self):
        print("Test no: 16")
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        home_page = HomePage(driver)
        ui_menu_url = home_page.get_link(27)
        driver.get(ui_menu_url)
        ui_menu = UiMenu(driver)
        time.sleep(1)
        ui_menu.download_pdf()
        time.sleep(2)
        print("---------------------------------")
        driver.quit()


    def test_java_alerts(self):
        print("Test no: 17")
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        home_page = HomePage(driver)
        java_alerts_url = home_page.get_link(28)
        driver.get(java_alerts_url)
        java_alerts = JavaAlerts(driver)
        time.sleep(1)
        java_alerts.click_js()
        time.sleep(2)
        print("---------------------------------")
        driver.quit()


    def test_data_tables(self):
        print("Test no: 18")
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        home_page = HomePage(driver)
        data_tables_url = home_page.get_link(40)
        driver.get(data_tables_url)
        data_tables = DataTables(driver)
        time.sleep(1)
        data_tables.print_elements()
        time.sleep(2)
        print("---------------------------------")
        driver.quit()

if __name__ == '__main__':
    unittest.main()