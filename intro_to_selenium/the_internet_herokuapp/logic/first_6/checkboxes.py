from intro_to_selenium.the_internet_herokuapp.infra.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckBoxes(BasePage):
    BOX_ONE = "//*[@id='checkboxes']/input[1]"
    BOX_TWO = "//*[@id='checkboxes']/input[2]"


    def __init__(self, driver):
        super().__init__(driver)
        self._box_one = self._driver.find_element(By.XPATH, self.BOX_ONE)
        self._box_two = self._driver.find_element(By.XPATH, self.BOX_TWO)



    def select_box_one(self):
        if not self._box_one.is_selected():
            self._box_one.click()
            print("checkbox one was filled")

    def select_box_two(self):
        if not self._box_two.is_selected():
            self._box_two.click()
            print("checkbox two was filled")


    def disable_box_one(self):
        if self._box_one.is_selected():
            self._box_one.click()
            print("checkbox one was disabled")


    def disable_box_two(self):
        if self._box_two.is_selected():
            self._box_two.click()
            print("checkbox two was disabled")
