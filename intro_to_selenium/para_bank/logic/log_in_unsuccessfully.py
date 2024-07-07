import logging
from intro_to_selenium.para_bank.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class LogInUnsuccessfully(BasePage):

    ERROR_MESSAGE = "//h1[text()='Error!']"


    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._error_message = self._driver.find_element(By.XPATH, self.ERROR_MESSAGE)
        except NoSuchElementException:
            logging.error(f'ELEMENT NOT FOUND: {e}')
        # an exception of not found element

    def log_in_failed(self):
        if self._error_message.is_displayed():
            logging.info("you have inserted wrong details, please try again")
            return True
        else:
            logging.info("error")
        # confirming function for invalid log in