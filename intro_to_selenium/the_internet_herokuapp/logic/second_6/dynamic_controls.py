from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from intro_to_selenium.the_internet_herokuapp.infra.base_page import BasePage
from selenium.webdriver.common.by import By
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')





class DynamicControls(BasePage):

    ENABLE_BTN = "//*[@id='input-example']/button"
    DISABLE_BTN = "//*[@id='input-example']/button"
    TEXT_BAR = "//input[@type='text']"
    WAITING = "//*[@id='loading']/img"

    def __init__(self, driver):
        super().__init__(driver)
        self._enable_btn = self._driver.find_element(By.XPATH, self.ENABLE_BTN)


    def enable_text_bar(self):
        self._enable_btn.click()

        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.WAITING)))

        disable_btn = WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.DISABLE_BTN)))
        if disable_btn.is_enabled():
            logging.info("disable btn is enabled")
        else:
            logging.info("disable btn is not enabled")

        text_bar = WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.TEXT_BAR)))
        if text_bar.is_enabled():
            logging.info("Text bar is enabled")
            text_bar.send_keys("positive")
        else:
            logging.info("Text bar is not enabled")

        disable_btn.click()
        print("disable btn was clicked")








