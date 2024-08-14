import logging
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_ui_projects.solarsystemscope.infra.base_page import BasePage
from selenium.webdriver.common.by import By



class DayLightMapPage(BasePage):
    # This class manages the DayLight page of the website.

    ADOBE_REQUEST_MESSAGE = "//a[contains(text(), 'Adobe Flash')]"


    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._adobe_request_message = self._driver.find_element(By.XPATH, self.ADOBE_REQUEST_MESSAGE)
        except NoSuchElementException:
            logging.error("ERROR MESSAGE element can not be found.")

    #------------------------------------------------------------------------------------------------------------
    # This function returns if the "Adobe Flash" request message is displayed.
    def adobe_request_message_display(self):
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ADOBE_REQUEST_MESSAGE)))
        if self._adobe_request_message.is_displayed():
            logging.info("REQUEST MESSAGE is displayed.")
            return self._adobe_request_message.text
        logging.error("REQUEST MESSAGE is not displayed.")
    #------------------------------------------------------------------------------------------------------------
