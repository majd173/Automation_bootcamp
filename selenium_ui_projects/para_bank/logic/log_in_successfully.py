from selenium_ui_projects.para_bank.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LogInSuccessfully(BasePage):

    TABLE_APPERANCE = "//table[@id='accountTable']"


    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._table_apperance = self._driver.find_element(By.XPATH, self.TABLE_APPERANCE)
        except NoSuchElementException as e:
            logging.error(f'ELEMENT NOT FOUND: {e}')
        # an exception of not found element

    def confirm_table(self):
        if self._table_apperance.is_displayed():
            logging.info("you are logged in")
            return True
        else:
            logging.info("you have inserted wrong details, please try again")
        # confirming function for valid log in
