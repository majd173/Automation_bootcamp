import logging
import time
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from intro_to_selenium.firefox_solarsystemscope.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class AstronomyPlacesPage(BasePage):
    # This class manages the Astronomy Places page in the website.

    MAP = "//div[@id='map']"
    LOAD_PLACES_BUTTON = "(//div[@class='btn-load-more-places-holder'])[1]"
    ADDED_BOX = "//div[contains(text(),'Planetarium Science Center')]"
    ERETZ_MUSEUM_BUTTON = "//a[@href='http://www.eretzmuseum.org.il/e/']"

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


    # This function returns if the map is displayed.
    def map_display(self):
        self._driver.execute_script("arguments[0].scrollIntoView();", self._map)
        time.sleep(2)
        if self._map.is_displayed():
            logging.info("MAP IS DISPLAYED.")
            return True
        logging.error("MAP IS NOT DISPLAYED.")

    #------------------------------------------------------------------------------------------------------------
    # This function click on "load Places" button.
    def click_on_load_places(self):
        self._driver.execute_script("arguments[0].scrollIntoView();", self._load_places)
        self._load_places.click()

    #------------------------------------------------------------------------------------------------------------
    # This function returns if the new distant places were have been added after running the previous function.
    def display_added_box(self):
        try:
            self._added_box = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, self.ADDED_BOX)))
            self._driver.execute_script("arguments[0].scrollIntoView();", self._added_box)
            time.sleep(2)
            if self._added_box.is_displayed():
                logging.info("ADDED BOX IS DISPLAYED.")
                return True
            print("ADDED BOX IS NOT DISPLAYED.")
        except NoSuchElementException:
            print("ADDED BOX ELEMENT CAN NOT BE FOUND.")

    #------------------------------------------------------------------------------------------------------------
    # This function clicks on the link of "Eretz Museum" and transfers to an external website.
    def click_on_eretz_museum_button(self):
        try:
            self._eretz_museum_button = WebDriverWait(self._driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, self.ERETZ_MUSEUM_BUTTON)))
            self._driver.execute_script("arguments[0].scrollIntoView();", self._eretz_museum_button)
            time.sleep(3)
            self._eretz_museum_button.click()
            time.sleep(3)
        except TimeoutException:
            print("ERETZ MUSEUM BUTTON CAN NOT BE FOUND OR PAGE DID NOT LOAD IN TIME.")
        except NoSuchElementException:
            print("ERETZ MUSEUM BUTTON CAN NOT BE FOUND.")
    #------------------------------------------------------------------------------------------------------------
