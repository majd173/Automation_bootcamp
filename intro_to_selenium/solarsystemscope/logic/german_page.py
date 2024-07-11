import logging
import time
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.solarsystemscope.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from intro_to_selenium.solarsystemscope.infra.config_provider import ConfigProvider
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class GermanPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def get_page_title(self, driver):
        time.sleep(3)
        return driver.title