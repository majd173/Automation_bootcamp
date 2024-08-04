from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from orange_hrm.ui.infra.base_page import BasePage
from selenium.webdriver.support.expected_conditions import *
import time

class HomePage(BasePage):


    MY_INFO = "a[href='/web/index.php/pim/viewMyDetails']"
    EMPLOYEE_FULL_NAME ="//p[@class='oxd-userdropdown-name']"

    def __init__(self, driver):
        super().__init__(driver)
        self._wait = WebDriverWait(self._driver, 10)

    def click_on_my_info(self):
        my_info = self._wait.until(EC.element_to_be_clickable
                                   ((By.XPATH, self.MY_INFO)))
        my_info.click()

    def get_full_name(self):
        employee_full_name = self._wait.until(EC.visibility_of_element_located
                                              ((By.XPATH, self.EMPLOYEE_FULL_NAME)))
        return employee_full_name.text.split(" ")

    def refresh_page(self):
        self._driver.refresh()







