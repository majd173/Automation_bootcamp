import logging
import time
from selenium.common import NoSuchElementException
from intro_to_selenium.firefox_solarsystemscope.infra.base_page import BasePage
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class DayLightMapPage(BasePage):
    # This class manages the DayLight page of the website.

    ADOBE_REQUEST_MESSAGE = "//a[contains(text(), 'Adobe Flash')]"


    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._adobe_request_message = self._driver.find_element(By.XPATH, self.ADOBE_REQUEST_MESSAGE)
        except NoSuchElementException:
            logging.error("ERROR MESSAGE ELEMENT CAN NOT BE FOUND.")

    #------------------------------------------------------------------------------------------------------------
    # This function returns if the "Adobe Flash" request message is displayed.
    def adobe_request_message_display(self):
        time.sleep(3)
        if self._adobe_request_message.is_displayed():
            logging.info("ERROR MESSAGE IS DISPLAYED.")
            return self._adobe_request_message.text
        logging.error("ERROR MESSAGE IS NOT DISPLAYED.")
    #------------------------------------------------------------------------------------------------------------
