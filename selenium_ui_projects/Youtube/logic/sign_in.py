from selenium_ui_projects.Youtube.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from selenium_ui_projects.Youtube.logic.utils import Utils
import logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class SignIn(BasePage):


    INPUT = "//input[@autocomplete='username']"
    NEXT_BUTTON = "//span[text()='Next']"


    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._input = self._driver.find_element(By.XPATH, self.INPUT)
            self._next_button = self._driver.find_element(By.XPATH, self.NEXT_BUTTON)
        except NoSuchElementException:
            logging.error("Element is not found.")


    def sign_in_flow(self):
        self._input.send_keys(Utils.generate_random_number(9))
        self._next_button.click()
