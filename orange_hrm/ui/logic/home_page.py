from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from orange_hrm.ui.base_page import BasePage
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.expected_conditions import *
from orange_hrm.ui.base_page import BasePage

class HomePage(BasePage):


    MY_INFO = "a[href='/web/index.php/pim/viewMyDetails']"


    def __init__(self, driver):
        super().__init__(driver)
        self._wait = WebDriverWait(self._driver, 10)

    def click_on_my_info(self):
        my_info = self._wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.MY_INFO)))
        my_info.click()




