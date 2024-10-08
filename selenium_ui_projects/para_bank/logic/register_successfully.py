from selenium_ui_projects.para_bank.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class RegisterSuccessfully(BasePage):

    SUCCESSFULLY_MESSAGE = "//p[text()='Your account was created successfully. You are now logged in.']"


    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._message = self._driver.find_element(By.XPATH, self.SUCCESSFULLY_MESSAGE)
        except NoSuchElementException as e:
            logging.error(f'ELEMENT NOT FOUND: {e}')
        # an exception of not found element
    def confirm_message(self):
        if self._message.is_displayed():
            logging.info('Your account was created successfully and you are now logged in.')
            return True
        else:
            logging.info('The success message is not displayed.')
        # confirming function for valid register