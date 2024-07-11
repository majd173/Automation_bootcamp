import logging
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from intro_to_selenium.solarsystemscope.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.expected_conditions import *
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class OnlineStorePage(BasePage):

    BASKET_BUTTON = "//a[@id='sprd-basket-button']"

    def __init__(self, driver):
        super().__init__(driver)
        # try:
        #     self._basket_button = self._driver.find_element(By.XPATH, self.BASKET_BUTTON)
        # except NoSuchElementException:
        #     logging.error("MEN TAB ELEMENT CAN NOT BE FOUND.")

    def click_on_basket_button(self):
        self._basket_button = self._driver.find_element(By.XPATH, self.BASKET_BUTTON)
        self._basket_button.click()




