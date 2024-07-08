from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.para_bank.infra.base_page import BasePage
from selenium.webdriver.common.by import By
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class LanguageList(BasePage):

    LANGUAGES_LIST = "//div[@id='submenu']//ytd-multi-page-menu-renderer//div[@class='menu-container style-scope ytd-multi-page-menu-renderer' and @id= 'container']"


    def __init__(self, driver):
        super().__init__(driver)


    def confirm_languages_pop_up_window(self):
        self._language_list = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.LANGUAGES_LIST)))
        if self._language_list.is_displayed():
            logging.info("-Keyboard shortcuts- is displayed")
            return True
        else:
            logging.info("-Keyboard shortcuts- is not displayed")
