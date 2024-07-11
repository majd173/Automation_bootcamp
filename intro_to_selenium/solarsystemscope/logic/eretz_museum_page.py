import logging
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from intro_to_selenium.solarsystemscope.infra.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.expected_conditions import *
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


class EretzMuseumPage(BasePage):

    HEADER_TITLE = "(//a[@href='https://www.eretzmuseum.org.il/en/'])[1]"

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self, driver):
        time.sleep(3)
        return driver.title




