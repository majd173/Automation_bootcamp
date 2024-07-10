import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.solarsystemscope.infra.base_page import BasePage
from selenium.webdriver.common.by import By
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class LogInUnsuccessfully(BasePage):


    ERROR_MESSAGE = "//div[contains(text(), 'Error:Email or password does not exist.')]"


    def __init__(self, driver):
        super().__init__(driver)


    def error_message_display(self):
        self._error_message = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ERROR_MESSAGE)))
        if self._error_message.is_displayed():
            logging.info("INVALID LOGIN DETAILS WERE INSERTED.")
            return self._error_message.text
        else:
            logging.error("AN ERROR OCCUERRED, ERROR MESSAGE SHOULD APPEAR.")









