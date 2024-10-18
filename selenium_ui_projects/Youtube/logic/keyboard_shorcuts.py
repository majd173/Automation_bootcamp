from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_ui_projects.Youtube.infra.base_page import BasePage
from selenium.webdriver.common.by import By
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class KeyboardShortcutsConfirm(BasePage):

    KEYBOARD_POP = "//ytd-hotkey-dialog-renderer[@class='style-scope ytd-popup-container']"


    def __init__(self, driver):
        super().__init__(driver)


    def confirm_keyboard_shortcuts_pop_up_window(self):
        self._keyboard = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.KEYBOARD_POP)))
        if self._keyboard.is_displayed():
            logging.info("-Keyboard shortcuts- is displayed")
            return True
        else:
            logging.info("-Keyboard shortcuts- is not displayed")

