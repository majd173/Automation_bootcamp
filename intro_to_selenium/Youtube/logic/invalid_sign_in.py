import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.para_bank.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')



class InvalidLogIn(BasePage):

    ERROR_SIGN = "//span[@class='AfGCob']"


    def __init__(self, driver):
        super().__init__(driver)
        # try:
        #     self._error_message = self._driver.find_element(By.XPATH, self.ERROR_MESSAGE)
        # except NoSuchElementException:
        #     logging.error("Element is not found.")

    def error_return(self):
        self._error_sign = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ERROR_SIGN)))
        if self._error_sign.is_displayed():
            logging.info("Inserted invalid Phone number")
            return True
        else:
            logging.info("Error")
