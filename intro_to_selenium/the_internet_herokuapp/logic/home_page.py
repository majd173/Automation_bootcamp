from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from intro_to_selenium.the_internet_herokuapp.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.the_internet_herokuapp.infra.config_provider import ConfigProvider
from intro_to_selenium.the_internet_herokuapp.infra.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver)
        self._driver = driver

    def get_link(self, index):
        links_elements = self._driver.find_elements(By.TAG_NAME, 'a')
        links = []
        for element in links_elements:
            links.append(element.get_attribute('href'))
        del links[0]
        del links[44]
        if index < len(links):
            return links[index]
        else:
            raise IndexError("Index out of range")








