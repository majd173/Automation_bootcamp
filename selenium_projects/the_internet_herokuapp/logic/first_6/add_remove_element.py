from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.the_internet_herokuapp.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class AddRemoveElement(BasePage):
    ADD_ELEMENT = "//*[@id='content']/div/button"
    DELETE_ELEMENT = "//button[@onclick='deleteElement()']"

    def __init__(self, driver):
        super().__init__(driver)
        self._add_element = self._driver.find_element(By.XPATH, self.ADD_ELEMENT)

    def add_element(self):
        self._add_element.click()
        try:
            delete_element = WebDriverWait(self._driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.DELETE_ELEMENT)))
            if delete_element.is_displayed():
                logging.info("Delete button is displayed")
                delete_element.click()
                logging.info("Delete button was clicked")
            else:
                logging.info("Delete button is not displayed")
        except TimeoutException:
            logging.info("Timed out waiting for delete button to appear")

    # def delete_element(self):
    #     self._delete_element.click()
