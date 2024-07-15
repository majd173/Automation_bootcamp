import logging
from intro_to_selenium.solarsystemscope.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OnlineAppsPage(BasePage):
    # This class manages the "Online Apps" page in the website.

    DAYLIGHT_MAP_BUTTON = "//a[@href='http://www.solarsystemscope.com/daylightmap']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._day_light_map = self._driver.find_element(By.XPATH, self.DAYLIGHT_MAP_BUTTON)
        except NoSuchElementException:
            logging.error("Day light map element can not be found.")
    # ------------------------------------------------------------------------------------------------------------
    # This function clicks on "DayLight Map" button.
    def click_on_day_light_map_button(self):
        WebDriverWait(self._driver,10).until(
            EC.element_to_be_clickable((By.XPATH, self.DAYLIGHT_MAP_BUTTON)))
        self._driver.execute_script("arguments[0].scrollIntoView();", self._day_light_map)
        self._day_light_map.click()

    #------------------------------------------------------------------------------------------------------------
