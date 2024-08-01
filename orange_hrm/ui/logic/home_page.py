from orange_hrm.ui.base_page import BasePage
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.expected_conditions import *
from orange_hrm.ui.base_page import BasePage
from orange_hrm.ui.config_provider import ConfigProvider

class HomePage(BasePage):


    MY_INFO = "a[href='/web/index.php/pim/viewMyDetails']"


    def __init__(self, driver):
        super().__init__(driver)

        try:
            self._my_info = self._driver.find_element(By.XPATH, self.MY_INFO)
        except NoSuchElementException:
            logging.error("An element can not be found")




