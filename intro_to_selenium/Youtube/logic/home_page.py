import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.para_bank.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.action_chains import ActionChains as AC
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class HomePage(BasePage):

    SIGN_IN_BUTTON = "//*[@id='buttons']/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div"
    SEARCH_BAR = "//input[@id='search']"
    SEARCH_BUTTON = "//button[@id='search-icon-legacy']"
    MENU_BUTTON = "//button[@aria-label='Guide']/yt-icon[@icon='yt-icons:menu']"
    MENU_LIST = "//ytd-mini-guide-renderer[@role='navigation']"
    YOUTUBE_KIDS = "//yt-formatted-string[text()='YouTube Kids']"
    HISTORY_Button = "//ytd-guide-entry-renderer//a[@title='History']"
    IM_A_KID = "//button[@aria-label='I'm a kid']"
    SETTINGS = "//yt-icon-button//button[@aria-label='Settings']"
    KEYBOARD_SHORTCUTS = "//yt-formatted-string[contains(text(),'Keyboard shortcuts')]"
    LANGUAGE = "//yt-formatted-string[contains(text(),'Language')]"


    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._sign_in_button = self._driver.find_element(By.XPATH, self.SIGN_IN_BUTTON)
            self._search_bar = self._driver.find_element(By.XPATH, self.SEARCH_BAR)
            self._search_button = self._driver.find_element(By.XPATH, self.SEARCH_BUTTON)
            self._menu_button = self._driver.find_element(By.XPATH, self.MENU_BUTTON)
            self._history = self._driver.find_element(By.XPATH, self.HISTORY_Button)
            self._settings = self._driver.find_element(By.XPATH, self.SETTINGS)
        except NoSuchElementException:
            logging.error("Element is not found.")


    def go_to_sign_in(self):
        sign_in_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.SIGN_IN_BUTTON)))
        # Scroll the element into view
        self._driver.execute_script("arguments[0].scrollIntoView(true);", sign_in_button)

        # Wait for the element to be clickable
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SIGN_IN_BUTTON))
        ).click()

    def search_bar_insert(self, input):
        self._search_bar.send_keys(input)

    def search_submit(self, input):
        self._search_bar.send_keys(input)
        self._search_button.click()
        return input


    def open_menu(self):
        self._menu_button.click()

    def go_to_history(self):
        self._history.click()


    def open_settings(self):
        self._settings.click()

    def open_keyboard_shortcuts(self):
        self._settings.click()
        self._keyboard_shortcuts = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.KEYBOARD_SHORTCUTS)))
        self._keyboard_shortcuts.click()


    def open_languages_list(self):
        self._settings.click()
        self._language = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.LANGUAGE)))
        self._language.click()



