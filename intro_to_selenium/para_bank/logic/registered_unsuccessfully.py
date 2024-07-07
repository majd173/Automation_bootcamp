from intro_to_selenium.para_bank.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class RegisterUsuccessfully(BasePage):

    ERROR_MESSAGE = "//span[text()='First name is required.']"


    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._error_message = self._driver.find_element(By.XPATH, self.ERROR_MESSAGE)
        except NoSuchElementException:
            logging.error(f'ELEMENT NOT FOUND: {e}')


    def register_failed(self):
        if self._error_message.is_displayed():
            logging.info("please insert valid username")
        else:
            logging.info("eror")
