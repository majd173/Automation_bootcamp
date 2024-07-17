import logging
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from intro_to_selenium.solarsystemscope.infra.base_page import BasePage
from selenium.webdriver.common.by import By



class EretzMuseumEventsPage(BasePage):


    EVENT_TAB = "//span[@class='ticker']"
    SPECIAL_EVENTS = "//span[contains(text(),'Special Events')]"


