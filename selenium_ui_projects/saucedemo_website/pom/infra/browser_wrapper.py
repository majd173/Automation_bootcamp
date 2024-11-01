import json

from selenium import webdriver

from selenium_ui_projects.saucedemo_website.pom.infra .config_provider import ConfigProvider


class BrowserWrapper:

    def __init__(self):
        self.driver = None
        self.config = ConfigProvider.load_from_file('../config.json')
        print("Test Start")

    def get_driver(self, url):
        if self.config["browser"] == "Chrome":
            self._driver = webdriver.Chrome()
        elif self.config["browser"] == "FireFox":
            self._driver = webdriver.Firefox()
        elif self.config["browser"] == "Edge":
            self._driver = webdriver.Edge()

        self._driver.get(url)
        self._driver.maximize_window()
        return self._driver
