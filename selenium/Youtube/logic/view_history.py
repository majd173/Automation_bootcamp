import logging
from selenium.Youtube.infra.base_page import BasePage
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ViewHistoryAsCustomer(BasePage):
    ERROR_MESSAGE = "//yt-formatted-string[@id='submessage']/span[1]"
    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._message_confirmation = self._driver.find_element(By.XPATH, self.ERROR_MESSAGE)
        except NoSuchElementException:
            logging.error("-Error message- element can not be found.")

    def return_error_message(self):
        if self._message_confirmation.is_displayed():
            logging.info("-Error message- is displayed")
            message_text = self._message_confirmation.text
            return message_text
        else:
            logging.info("-Error message- is not displayed")