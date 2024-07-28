import logging
import time

from selenium.common import NoSuchElementException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_projects.solarsystemscope.infra.base_page import BasePage
from selenium.webdriver.common.by import By


class EretzMuseumPage(BasePage):
    FIRST_DOT_BEFORE_CLICK = "(//button[@class='owl-dot'])[1]"
    SECOND_DOT_BEFORE_CLICK = "(//button[@class='owl-dot'])[1]"
    THIRD_DOT_BEFORE_CLICK = "(//button[@class='owl-dot'])[2]"
    FORTH_DOT_BEFORE_CLICK = "(//button[@class='owl-dot'])[3]"
    DOT_AFTER_CLICK = "//button[@class='owl-dot active']"
    TICKETS_BUTTON = "//header//a[contains(text(),'Tickets')]"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._first_dot = self._driver.find_element(By.XPATH, self.FIRST_DOT_BEFORE_CLICK)
        except NoSuchElementException:
            logging.error("FIRST DOT element can not be found.")
        try:
            self._second_dot = self._driver.find_element(By.XPATH, self.SECOND_DOT_BEFORE_CLICK)
        except NoSuchElementException:
            logging.error("SECOND DOT element can not be found.")
        try:
            self._third_dot = self._driver.find_element(By.XPATH, self.THIRD_DOT_BEFORE_CLICK)
        except NoSuchElementException:
            logging.error("THIRD DOT element can not be found.")
        try:
            self._forth_dot = self._driver.find_element(By.XPATH, self.FORTH_DOT_BEFORE_CLICK)
        except NoSuchElementException:
            logging.error("FORTH DOT element can not be found.")
        try:
            self._tickets_button = self._driver.find_element(By.XPATH, self.TICKETS_BUTTON)
        except NoSuchElementException:
            logging.error("TICKETS element can not be found.")

    #------------------------------------------------------------------------------------------------------------

    def click_on_dots(self):
        try:
            self._dot_clicked = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.DOT_AFTER_CLICK)))
            if self._dot_clicked.is_displayed():
                self._second_dot.click()
                time.sleep(1)
                self._third_dot.click()
                time.sleep(1)
                self._forth_dot.click()
                time.sleep(1)
                return 'Dots were clicked'
            logging.error("An error occured")
        except Exception:
            logging.error("An error occured.")

    #------------------------------------------------------------------------------------------------------------

    def check_dot_clickable(self):
        self._dot_clicked = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.DOT_AFTER_CLICK)))

        if self._dot_clicked.is_displayed():
            WebDriverWait(self._driver, 5)
            logging.info("Dots were clicked successfully")
            return True
        logging.error("Dots were clicked.")
        return False

    #------------------------------------------------------------------------------------------------------------

    def click_tickets_button(self):
        self._tickets_button.click()

    #------------------------------------------------------------------------------------------------------------


    def window_switch(self, current_window):
        try:
            assert len(self._driver.window_handles) == 2
            self.click_tickets_button()
            WebDriverWait(self._driver, 10).until(EC.number_of_windows_to_be(3))
            for window_handle in self._driver.window_handles:
                if window_handle != current_window:
                    self._driver.switch_to.window(window_handle)
                    logging.info("Window was switched successfully.")
                    break
        except WebDriverException:
            logging.error("Can not switch to the eretz museum events window.")

    #------------------------------------------------------------------------------------------------------------




