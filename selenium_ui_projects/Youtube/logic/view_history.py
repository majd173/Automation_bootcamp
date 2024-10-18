import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_ui_projects.Youtube.infra.base_page import BasePage

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ViewHistoryAsCustomer(BasePage):
    ERROR_MESSAGE = "//yt-formatted-string[@id='submessage']/span[1]"

    def __init__(self, driver):
        super().__init__(driver)
        # try:
        #     self._message_confirmation = self._driver.find_element(By.CSS_SELECTOR, self.ERROR_MESSAGE)
        # except NoSuchElementException:
        #     logging.error("-Error message- element can not be found.")

    def return_error_message(self):
        message_confirmation = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ERROR_MESSAGE)))
        if message_confirmation.is_displayed():
            logging.info("-Error message- is displayed")
            message_text = message_confirmation.text
            return message_text
        else:
            logging.info("-Error message- is not displayed")
