import logging
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from intro_to_selenium.solarsystemscope.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.expected_conditions import *
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class OrganicProductsPage(BasePage):


    HEADER_TITLE = "//h1[contains(text(), 'Men - Organic Products')]"


    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._header_title = self._driver.find_element(By.XPATH, self.HEADER_TITLE)
        except NoSuchElementException:
            logging.error("HEADER TITLE ELEMENT CAN NOT BE FOUND.")

    def header_title_display(self):
        if self._header_title.is_displayed():
            logging.info("HEADER TITLE IS DISPLAYED.")
            return self._header_title.text
        logging.error("HEADER TITLE IS NOT DISPLAED.")




