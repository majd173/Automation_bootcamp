from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.Youtube.infra.base_page import BasePage
from selenium.webdriver.common.by import By
import logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class SearchSubmit(BasePage):
    SEARCH_RESULT = "//a[contains(@title,'Best of Michael Jordan')]" # For search_test
    SEARCH_RESULT_2 = "//a[@title='Why we all need subtitles now']" # For subtitles_test

    def __init__(self, driver):
        super().__init__(driver)

    # For search_test
    def search_and_confirm_result(self):
        self._search_result = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.SEARCH_RESULT)))
        result_text = self._search_result.text
        return result_text


    # Foe subtitles_result (also opens any video search by importing a locator)
    def open_video(self):
        self._search_result_2 = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.SEARCH_RESULT_2))).click()
        return self._search_result_2






