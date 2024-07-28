import time
import unittest
from selenium.the_internet_herokuapp.infra.config_provider import ConfigProvider
from selenium.the_internet_herokuapp.infra.browser_wrapper import BrowserWrapper
from selenium.the_internet_herokuapp.logic.home_page import HomePage
# Tests
from selenium.the_internet_herokuapp.logic.first_6.add_remove_element import AddRemoveElement
from selenium.the_internet_herokuapp.logic.first_6.broken_image import BrokenImage
from selenium.the_internet_herokuapp.logic.first_6.checkboxes import CheckBoxes
from selenium.the_internet_herokuapp.logic.first_6.context_menu import ContextMenu
from selenium.the_internet_herokuapp.logic.first_6.disappearing_elements import DisappearingElements
from selenium.the_internet_herokuapp.logic.first_6.drag_and_drop import DragAndDrop

class TestSite(unittest.TestCase):

    def setUp(self):
        config = ConfigProvider.load_from_file('../config.json')
        self.driver = BrowserWrapper().get_driver(config["base_url"])
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_add_remove_elements(self):
        print("Test no: 1")
        self.driver.get(self.home_page.get_link(1))
        add_remove_element = AddRemoveElement(self.driver)
        add_remove_element.add_element()
        # add_remove_element.add_element()
        # time.sleep(1)
        print("---------------------------------")

    def test_broken_images(self):
        print("Test no: 2")
        self.driver.get(self.home_page.get_link(3))
        broken_images = BrokenImage(self.driver)
        broken_images.check_picture_display()
        print("---------------------------------")


    def test_checkboxes_enabling(self):
        print("Test no: 3")
        self.driver.get(self.home_page.get_link(5))
        check_page = CheckBoxes(self.driver)
        check_page.select_box_one()
        check_page.disable_box_two()
        print("---------------------------------")


    def test_context_menu(self):
        print("Test no: 4")
        self.driver.get(self.home_page.get_link(6))
        context_menu = ContextMenu(self.driver)
        context_menu.right_click_test()
        print("---------------------------------")
        # driver.quit()

    def test_disappearing_elements(self):
        print("Test no: 5")
        self.driver.get(self.home_page.get_link(8))
        disappearing_elements = DisappearingElements(self.driver)
        disappearing_elements.check_gallery_apperance()
        self.driver.refresh()
        print("---------------------------------")

    def test_drag_and_drop(self):
        print("Test no: 6")
        self.driver.get(self.home_page.get_link(9))
        drag_and_drop = DragAndDrop(self.driver)
        drag_and_drop.drag_and_drop()
        print("---------------------------------")


if __name__ == '__main__':
    unittest.main()