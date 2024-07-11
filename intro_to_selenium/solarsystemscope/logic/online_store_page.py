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

    MEN_TAB = "//div[@id='department-filter-D1']"
    ORGANIC_PRODUCTS_BUTTON = "//a[@href='/men+organic+products?q=P29']"

    def __init__(self, driver):
        super().__init__(driver)
        # try:
        #     self._men_tab = self._driver.find_element(By.XPATH, self.MEN_TAB)
        # except NoSuchElementException:
        #     logging.error("MEN TAB ELEMENT CAN NOT BE FOUND.")

    def hover_on_men_tab(self):
        try:
            actions = AC(self._driver)
            self._men_tab = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.MEN_TAB)))
            actions.move_to_element(self._men_tab).perform()
            time.sleep(2)
            self._organic_products_button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.ORGANIC_PRODUCTS_BUTTON)))
            actions.move_to_element(self._organic_products_button).click().perform()
            time.sleep(3)
        except NoSuchElementException:
            logging.info("MEN TAB ELEMENT CAN NOT BE FOUND.")


    # def click_on_organic_products_button(self):
    #     try:
    #         actions = AC(self._driver)
    #         self._organic_products_button = WebDriverWait(self._driver, 10).until(
    #             EC.visibility_of_element_located((By.XPATH, self.ORGANIC_PRODUCTS_BUTTON)))
    #         actions.move_to_element(self._organic_products_button).click().perform()
    #         time.sleep(3)
    #     except NoSuchElementException:
    #         logging.error("ORGANIC PRODUCTS ELEMENT CAN NOT BE FOUND.")
