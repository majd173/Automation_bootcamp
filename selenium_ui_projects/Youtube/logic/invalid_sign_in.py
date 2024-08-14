import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.Youtube.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')



class InvalidLogIn(BasePage):

    ERROR_SIGN = "//span[@class='AfGCob']"


    def __init__(self, driver):
        super().__init__(driver)


    def error_return(self):
        self._error_sign = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ERROR_SIGN)))
        if self._error_sign.is_displayed():
            logging.info("Inserted invalid Phone number")
            return True
        else:
            logging.info("Error")
