from selenium_ui_projects.para_bank.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from selenium_ui_projects.para_bank.infra.utils import Utils
import logging


class Register(BasePage):
    FIRST_NAME = "//input[@id='customer.firstName']"
    LAST_NAME = "//input[@id='customer.lastName']"
    ADDRESS = "//input[@id='customer.address.street']"
    CITY = "//input[@id='customer.address.city']"
    STATE = "//input[@id='customer.address.state']"
    ZIP_CODE = "//input[@id='customer.address.zipCode']"
    PHONE = "//input[@id='customer.phoneNumber']"
    SSN = "//input[@id='customer.ssn']"
    USERNAME = "//input[@id='customer.username']"
    PASSWORD = "//input[@id='customer.password']"
    CONFIRM = "//input[@id='repeatedPassword']"
    REGISTER_BTN = "//input[@value='Register']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._first_name = self._driver.find_element(By.XPATH, self.FIRST_NAME)
            self._last_name = self._driver.find_element(By.XPATH, self.LAST_NAME)
            self._address = self._driver.find_element(By.XPATH, self.ADDRESS)
            self._city = self._driver.find_element(By.XPATH, self.CITY)
            self._state = self._driver.find_element(By.XPATH, self.STATE)
            self._zip_code = self._driver.find_element(By.XPATH, self.ZIP_CODE)
            self._phone = self._driver.find_element(By.XPATH, self.PHONE)
            self._ssn = self._driver.find_element(By.XPATH, self.SSN)
            self._username = self._driver.find_element(By.XPATH, self.USERNAME)
            self._password = self._driver.find_element(By.XPATH, self.PASSWORD)
            self._confirm = self._driver.find_element(By.XPATH, self.CONFIRM)
            self._register_btn = self._driver.find_element(By.XPATH, self.REGISTER_BTN)
        except NoSuchElementException as e:
            logging.error(f'ELEMENT NOT FOUND: {e}')
        # an exception of not found element

    def insert_first_name(self):
        self._first_name.send_keys(Utils.generate_random_string(5))

    def insert_last_name(self):
        self._last_name.send_keys(Utils.generate_random_string(5))

    def insert_address(self,):
        self._address.send_keys(Utils.generate_random_string(5))

    def insert_city(self):
        self._city.send_keys(Utils.generate_random_string(5))

    def insert_state(self):
        self._state.send_keys(Utils.generate_random_string(5))

    def insert_zip_code(self):
        self._zip_code.send_keys(Utils.generate_random_number(7))

    def insert_phone(self):
        self._phone.send_keys(Utils.generate_random_number(10))

    def insert_ssn(self):
        self._ssn.send_keys(Utils.generate_random_number(15))

    def insert_username(self):
        self._username.send_keys(Utils.generate_random_string(5))

    def insert_password(self, password):
        self._password.send_keys(password)

    def insert_password_confirm(self, password):
        self._confirm.send_keys(password)

    def click_register_btn(self):
        self._register_btn.click()

    def valid_register_flow(self):
        password = Utils.generate_random_string(7)
        self.insert_first_name()
        self.insert_last_name()
        self.insert_address()
        self.insert_city()
        self.insert_state()
        self.insert_zip_code()
        self.insert_phone()
        self.insert_ssn()
        self.insert_username()
        self.insert_password(password)
        self.insert_password_confirm(password)
        self.click_register_btn()
        # valid registration process
    def invalid_register_flow(self):
        password = Utils.generate_random_string(7)
        self.insert_last_name()
        self.insert_address()
        self.insert_city()
        self.insert_state()
        self.insert_zip_code()
        self.insert_phone()
        self.insert_ssn()
        self.insert_username()
        self.insert_password(password)
        self.insert_password_confirm(password)
        self.click_register_btn()
        # this function does not insert first name (invalid register)
