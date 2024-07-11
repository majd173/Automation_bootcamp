import logging
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from intro_to_selenium.solarsystemscope.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.expected_conditions import *
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class OnlineAppsPage(BasePage):

    DAYLIGHT_MAP_BUTTON = "//a[@href='http://www.solarsystemscope.com/daylightmap']"


    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._day_light_map = self._driver.find_element(By.XPATH, self.DAYLIGHT_MAP_BUTTON)
        except NoSuchElementException:
            logging.error("DAY LIGHT MAP ELEMENT CAN NOT BE FOUND.")

    def click_on_day_light_map_button(self):
        self._day_light_map.click()
        time.sleep(4)