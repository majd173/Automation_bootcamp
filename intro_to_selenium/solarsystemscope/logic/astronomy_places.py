import logging
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from intro_to_selenium.solarsystemscope.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *


# logging.basicConfig(
#     filename="solar_logfile.log",
#     format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S', filemode='w')


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
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.MAP)))
        self._driver.execute_script("arguments[0].scrollIntoView();", self._map)
        if self._map.is_displayed():
            logging.info("MAP IS DISPLAYED.")
            self._driver.save_screenshot('Astronomy places map display.png')
            return True
        logging.error("MAP IS NOT DISPLAYED.")

    #------------------------------------------------------------------------------------------------------------
    # This function click on "load Places" button.
    def click_on_load_places(self):
        self._driver.execute_script("arguments[0].scrollIntoView();", self._load_places)
        self._driver.save_screenshot('Before opening Distant places list.png')
        self._load_places.click()
        logging.info("LOAD PLACES BUTTON WAS CLICKED.")

    #------------------------------------------------------------------------------------------------------------
    # This function returns if the new distant places were have been added after running the previous function.
    def display_added_box(self):
        try:
            self._added_box = WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, self.ADDED_BOX)))
            self._driver.execute_script("arguments[0].scrollIntoView();", self._added_box)
            if self._added_box.is_displayed():
                logging.info("ADDED BOX IS DISPLAYED.")
                self._driver.save_screenshot('After opening Distant places list.png')
                return True
            logging.info("ADDED BOX IS NOT DISPLAYED.")
        except NoSuchElementException:
            logging.error("ADDED BOX ELEMENT CAN NOT BE FOUND.")

    #------------------------------------------------------------------------------------------------------------
    # This function clicks on the link of "Eretz Museum" and transfers to an external website.
    def click_on_eretz_museum_button(self):
        try:
            self._eretz_museum_button = WebDriverWait(self._driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, self.ERETZ_MUSEUM_BUTTON)))
            self._driver.save_screenshot('Before clicking on Eretz Museum button.png')
            self._eretz_museum_button.click()
            logging.info("ERETZ MUSEUM BUTTON WAS CLICKED.")
        except TimeoutException:
            logging.error("ERETZ MUSEUM BUTTON CAN NOT BE FOUND OR PAGE DID NOT LOAD IN TIME.")
        except NoSuchElementException:
            logging.error("ERETZ MUSEUM BUTTON CAN NOT BE FOUND.")

    #------------------------------------------------------------------------------------------------------------
    # This function switches from an opened window to another one by inserting the current window.
    def window_switch(self, current_window):
        try:
            assert len(self._driver.window_handles) == 1
            self.click_on_eretz_museum_button()
            WebDriverWait(self._driver, 10).until(EC.number_of_windows_to_be(2))
            for window_handle in self._driver.window_handles:
                if window_handle != current_window:
                    self._driver.switch_to.window(window_handle)
                    break
        except WebDriverException:
            logging.error("CAN NOT SWITCH TO THE ERETZ MUSEUM WINDOW.")

    #------------------------------------------------------------------------------------------------------------
