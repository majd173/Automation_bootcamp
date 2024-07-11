import logging
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from intro_to_selenium.solarsystemscope.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.expected_conditions import *
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class AstronomyPlacesPage(BasePage):

    MAP = "//div[@id='map']"
    LOAD_PLACES_BUTTON = "(//div[@class='btn-load-more-places-holder'])[1]"
    ADDED_BOX = "(//div[@class='place-box'])[6]"


    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._map = self._driver.find_element(By.XPATH, self.MAP)
        except NoSuchElementException:
            logging.error("MAP ELEMENT CAN NOT BE FOUND.")
        try:
            self._load_places = self._driver.find_element(By.XPATH, self.LOAD_PLACES_BUTTON)
        except NoSuchElementException:
            logging.error("LOAD PLACES ELEMENT CAN NOT BE FOUND.")


    def map_display(self):
        if self._map.is_displayed():
            logging.info("MAP IS DISPLAYED.")
            return True
        logging.error("MAP IS NOT DISPLAYED.")

    def click_on_load_places(self):
        self._driver.execute_script("arguments[0].scrollIntoView();", self._load_places)
        self._load_places.click()
    def display_added_box(self):
        try:
            self._added_box = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, self.ADDED_BOX)))
            if self._added_box.is_displayed():
                logging.info("ADDED BOX IS DISPLAYED.")
                return True
            print("ADDED BOX IS NOT DISPLAYED.")
        except NoSuchElementException:
            print("ADDED BOX ELEMENT CAN NOT BE FOUND.")
