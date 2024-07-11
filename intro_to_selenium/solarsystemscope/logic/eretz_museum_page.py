import logging
import time
from selenium.webdriver.chrome.webdriver import WebDriver

from intro_to_selenium.solarsystemscope.infra.base_page import BasePage
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class EretzMuseumPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    def get_page_url(self):
        return self._driver.current_url




