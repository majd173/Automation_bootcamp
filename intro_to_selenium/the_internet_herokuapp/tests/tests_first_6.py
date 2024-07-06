import time
import unittest
from intro_to_selenium.the_internet_herokuapp.infra.config_provider import ConfigProvider
from intro_to_selenium.the_internet_herokuapp.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.the_internet_herokuapp.logic.home_page import HomePage
# Tests
from intro_to_selenium.the_internet_herokuapp.logic.first_6.add_remove_element import AddRemoveElement
from intro_to_selenium.the_internet_herokuapp.logic.first_6.broken_image import BrokenImage
from intro_to_selenium.the_internet_herokuapp.logic.first_6.checkboxes import CheckBoxes
from intro_to_selenium.the_internet_herokuapp.logic.first_6.context_menu import ContextMenu
from intro_to_selenium.the_internet_herokuapp.logic.first_6.disappearing_elements import DisappearingElements
from intro_to_selenium.the_internet_herokuapp.logic.first_6.drag_and_drop import DragAndDrop

class TestSite(unittest.TestCase):

    # def setUp(self):
    #     config = ConfigProvider.load_from_file('../config.json')
    #     self.driver = BrowserWrapper().get_driver(config["base_url"])
    #     self.home_page = HomePage(self.driver)
    #
    # def tearDown(self):
    #     self.driver.quit()

    def test_add_remove_elements(self):
        print("Test no: 1")
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        home_page = HomePage(driver)
        add_remove_element = home_page.get_link(1)
        driver.get(add_remove_element)
        add_remove_element = AddRemoveElement(driver)
        time.sleep(1)
        add_remove_element.add_element()
        time.sleep(1)
        # add_remove_element.add_element()
        # time.sleep(1)
        print("---------------------------------")
        driver.quit()

    def test_broken_images(self):
        print("Test no: 2")
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        home_page = HomePage(driver)
        broken_images = home_page.get_link(3)
        driver.get(broken_images)
        broken_images = BrokenImage(driver)
        time.sleep(1)
        broken_images.check_picture_display()
        print("---------------------------------")
        driver.quit()


    def test_checkboxes_enabling(self):
        print("Test no: 3")
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        home_page = HomePage(driver)
        checkbox_link = home_page.get_link(5)
        driver.get(checkbox_link)
        check_page = CheckBoxes(driver)
        time.sleep(1)
        check_page.select_box_one()
        time.sleep(1)
        check_page.disable_box_two()
        time.sleep(1)
        print("---------------------------------")
        driver.quit()


    def test_context_menu(self):
        print("Test no: 4")
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        home_page = HomePage(driver)
        context_menu = home_page.get_link(6)
        driver.get(context_menu)
        context_menu = ContextMenu(driver)
        time.sleep(1)
        context_menu.right_click_test()
        time.sleep(2)
        print("---------------------------------")
        driver.quit()

    def test_disappearing_elements(self):
        print("Test no: 5")
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        home_page = HomePage(driver)
        disappearing_elements = home_page.get_link(8)
        driver.get(disappearing_elements)
        disappearing_elements = DisappearingElements(driver)
        time.sleep(1)
        disappearing_elements.check_gallery_apperance()
        time.sleep(1)
        driver.refresh()
        time.sleep(1)
        print("---------------------------------")
        driver.quit()

    def test_drag_and_drop(self):
        print("Test no: 6")
        config = ConfigProvider.load_from_file('../config.json')
        driver = BrowserWrapper().get_driver(config["base_url"])
        home_page = HomePage(driver)
        drag_and_drop = home_page.get_link(9)
        driver.get(drag_and_drop)
        drag_and_drop = DragAndDrop(driver)
        time.sleep(1)
        drag_and_drop.drag_and_drop()
        time.sleep(2)
        print("---------------------------------")
        driver.quit()


if __name__ == '__main__':
    unittest.main()