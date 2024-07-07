import logging
from intro_to_selenium.para_bank.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from intro_to_selenium.para_bank.infra.utils import Utils


class HomePage(BasePage):
    REGISTER = "//a[text()='Register']"
    REGISTER_PAGE = "//h1[text()='Signing up is easy!']"
    USERNAME_INPUT = "//input[@name='username']"
    PASSWORD_INPUT = "//input[@name='password']"
    LOG_IN_BTN = "//input[@value='Log In']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._register = self._driver.find_element(By.XPATH, self.REGISTER)
            self._username_input = self._driver.find_element(By.XPATH, self.USERNAME_INPUT)
            self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
            self._log_in_btn = self._driver.find_element(By.XPATH, self.LOG_IN_BTN)
        except NoSuchElementException as e:
            logging.error(f'ELEMENT NOT FOUND: {e}')

    def insert_username(self, username):
        self._username_input.send_keys(username)

    def insert_password(self, password):
        self._password_input.send_keys(password)

    def click_log_in_btn(self):
        self._log_in_btn.click()

    def go_to_register(self):
        self._register.click()



    def valid_login_flow(self, username, password):
        self.insert_username(username)
        self.insert_password(password)
        self.click_log_in_btn()

    def invalid_log_in_flow(self):
        self.insert_username(" ")
        self.insert_password(Utils.generate_random_string(7))
        self.click_log_in_btn()
