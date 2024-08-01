from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.by import By
import logging
from orange_hrm.ui.base_page import BasePage
from orange_hrm.ui.config_provider import ConfigProvider

class LogInPage(BasePage):


    USERNAME_INPUT = "input[placeholder='Username']"
    PASSWORD_INPUT = "input[placeholder='Password']"
    LOGIN_BUTTON = "button[type='submit']"


    def __init__(self, driver):
        super().__init__(driver)
        self._config = ConfigProvider.load_from_file("orange_hrm.json")
        try:
            self._username_input = self._driver.find_element(By.XPATH, self.USERNAME_INPUT)
            self._password_input = self._driver.find_element(BY.XPATH, self.PASSWORD_INPUT)
            self._login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)
        except NoSuchElementException:
            logging.error("An element can not be found")



    def insert_username(self):
        self._username_input.send_keys(self._config["username"])

    def insert_password(self):
        self._password_input.send_keys(self._config["password"])

    def click_log_in_btn(self):
        self._login_button.click()


    def login_flow(self):
        self.insert_username()
        self.insert_password()
        self.click_log_in_btn()